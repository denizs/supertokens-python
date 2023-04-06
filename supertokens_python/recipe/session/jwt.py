# Copyright (c) 2021, VRAI Labs and/or its affiliates. All rights reserved.
#
# This software is licensed under the Apache License, Version 2.0 (the
# "License") as published by the Apache Software Foundation.
#
# You may not use this file except in compliance with the License. You may
# obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import base64
import json
from base64 import b64decode
from json import dumps, loads
from textwrap import wrap
from typing import Any, Dict, Optional

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from supertokens_python.utils import utf_base64decode, utf_base64encode

_key_start = "-----BEGIN PUBLIC KEY-----\n"
_key_end = "\n-----END PUBLIC KEY-----"

"""
why separators is used in dumps:
- without it's use, output of dumps is: '{"alg": "RS256", "typ": "JWT", "version": "1"}'
- with it's use, output of dumps is: '{"alg":"RS256","typ":"JWT","version":"1"}'

we require the non-spaced version, else the base64 encoding string will end up different than required
"""
_allowed_headers = [
    utf_base64encode(
        dumps(
            {"alg": "RS256", "typ": "JWT", "version": "2"},
            separators=(",", ":"),
            sort_keys=True,
        )
    )
]


class ParsedJWTInfo:
    def __init__(
        self,
        version: int,
        raw_token_string: str,
        raw_payload: str,
        header: str,
        payload: Dict[str, Any],
        signature: str,
        kid: Optional[str],
    ) -> None:
        self.version = version
        self.raw_token_string = raw_token_string
        self.raw_payload = raw_payload
        self.header = header
        self.payload = payload
        self.signature = signature
        self.kid = kid


def parse_jwt_without_signature_verification(jwt: str) -> ParsedJWTInfo:
    splitted_input = jwt.split(".")
    if len(splitted_input) != 3:
        raise Exception("invalid jwt")

    # V1 and V2 are functionally identical, plus all legacy tokens should be V2 now.
    # So we can assume these defaults:
    version = 2
    kid = None
    # V2 or older tokens didn't save the key id
    header, payload, signature = splitted_input
    # checking the header
    if header not in _allowed_headers:
        parsed_header = json.loads(base64.b64decode(header.encode()))
        header_version = parsed_header.get("version")

        # We have to ensure version is a string, otherwise Number.parseInt can have unexpected results
        if not isinstance(header_version, str):
            raise Exception("JWT header mismatch")

        try:
            version = int(header_version)
        except ValueError:
            version = None

        kid = parsed_header.get("kid")
        # Number.isInteger returns false for Number.NaN (if it fails to parse the version)
        if (
            parsed_header["typ"] != "JWT"
            or not isinstance(version, int)
            or version < 3
            or kid is None
        ):
            raise Exception("JWT header mismatch")

    return ParsedJWTInfo(
        version=version,
        raw_token_string=jwt,
        raw_payload=payload,
        header=header,
        # Ideally we would only parse this after the signature verification is done
        # We do this at the start, since we want to check if a token can be a supertokens access token or not.
        payload=loads(utf_base64decode(payload)),
        signature=signature,
        kid=kid,  # TODO: How can ever be None since we are checking for it in the above code?
    )


# TODO: Should remove
def verify_jwt(info: ParsedJWTInfo, jwt_signing_public_key: str):
    public_key = RSA.import_key(
        _key_start + "\n".join(wrap(jwt_signing_public_key, width=64)) + _key_end
    )
    verifier = PKCS115_SigScheme(public_key)
    to_verify = SHA256.new((info.header + "." + info.raw_payload).encode("utf-8"))
    try:
        verifier.verify(to_verify, b64decode(info.signature.encode("utf-8")))
    except BaseException:
        raise Exception("jwt verification failed")
