from ...jwt.interfaces import CreateJwtResult as CreateJwtResult, GetJWKSResult as GetJWKSResult
from ..interfaces import SessionContainer as SessionContainer, SessionInformationResult as SessionInformationResult
from supertokens_python.async_to_sync_wrapper import sync as sync
from supertokens_python.recipe.openid.interfaces import GetOpenIdDiscoveryConfigurationResult as GetOpenIdDiscoveryConfigurationResult
from typing import Any, Dict, List, Union

def create_new_session(request: Any, user_id: str, access_token_payload: Union[Dict[str, Any], None] = ..., session_data: Union[Dict[str, Any], None] = ..., user_context: Union[None, Dict[str, Any]] = ...) -> SessionContainer: ...
def get_session(request: Any, anti_csrf_check: Union[bool, None] = ..., session_required: bool = ..., user_context: Union[None, Dict[str, Any]] = ...) -> Union[SessionContainer, None]: ...
def refresh_session(request: Any, user_context: Union[None, Dict[str, Any]] = ...) -> SessionContainer: ...
def revoke_session(session_handle: str, user_context: Union[None, Dict[str, Any]] = ...) -> bool: ...
def revoke_all_sessions_for_user(user_id: str, user_context: Union[None, Dict[str, Any]] = ...) -> List[str]: ...
def revoke_multiple_sessions(session_handles: List[str], user_context: Union[None, Dict[str, Any]] = ...) -> List[str]: ...
def get_session_information(session_handle: str, user_context: Union[None, Dict[str, Any]] = ...) -> SessionInformationResult: ...
def update_session_data(session_handle: str, new_session_data: Dict[str, Any], user_context: Union[None, Dict[str, Any]] = ...) -> None: ...
def update_access_token_payload(session_handle: str, new_access_token_payload: Dict[str, Any], user_context: Union[None, Dict[str, Any]] = ...) -> None: ...
def create_jwt(payload: Dict[str, Any], validity_seconds: Union[None, int] = ..., user_context: Union[None, Dict[str, Any]] = ...) -> CreateJwtResult: ...
def get_jwks(user_context: Union[None, Dict[str, Any]] = ...) -> GetJWKSResult: ...
def get_open_id_discovery_configuration(user_context: Union[None, Dict[str, Any]] = ...) -> GetOpenIdDiscoveryConfigurationResult: ...
def regenerate_access_token(access_token: str, new_access_token_payload: Union[Dict[str, Any], None] = ..., user_context: Union[None, Dict[str, Any]] = ...): ...
