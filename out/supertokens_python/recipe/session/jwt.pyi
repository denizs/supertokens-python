from supertokens_python.utils import utf_base64decode as utf_base64decode, utf_base64encode as utf_base64encode
from typing import Any, Dict

def get_payload(jwt: str, signing_public_key: str): ...
def get_payload_without_verifying(jwt: str) -> Dict[str, Any]: ...
