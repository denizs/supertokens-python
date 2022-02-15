from .types import ErrorFormField as ErrorFormField
from supertokens_python.exceptions import SuperTokensError as SuperTokensError
from typing import Any, Dict, List

def raise_form_field_exception(msg: str, form_fields: List[ErrorFormField]): ...

class SuperTokensEmailPasswordError(SuperTokensError): ...

class FieldError(SuperTokensEmailPasswordError):
    form_fields: Any
    def __init__(self, msg: str, form_fields: List[ErrorFormField]) -> None: ...
    def get_json_form_fields(self) -> List[Dict[str, Any]]: ...
