from ..emailverification.types import User as EmailVerificationUser
from .interfaces import APIInterface as APIInterface, RecipeInterface as RecipeInterface
from .provider import Provider as Provider
from .recipe import ThirdPartyRecipe as ThirdPartyRecipe
from .types import User as User
from supertokens_python.exceptions import raise_bad_input_exception as raise_bad_input_exception
from supertokens_python.recipe.emailverification.utils import OverrideConfig as EmailVerificationOverrideConfig, ParentRecipeEmailVerificationConfig as ParentRecipeEmailVerificationConfig
from typing import Any, Awaitable, Callable, Dict, List, Union

class SignInAndUpFeature:
    providers: Any
    def __init__(self, providers: List[Provider]): ...

class InputEmailVerificationConfig:
    get_email_verification_url: Any
    create_and_send_custom_email: Any
    def __init__(self, get_email_verification_url: Union[Callable[[User, Any], Awaitable[str]], None] = ..., create_and_send_custom_email: Union[Callable[[User, str, Any], Awaitable[None]], None] = ...) -> None: ...

def email_verification_create_and_send_custom_email(recipe: ThirdPartyRecipe, create_and_send_custom_email: Callable[[User, str, Dict[str, Any]], Awaitable[None]]) -> Callable[[EmailVerificationUser, str, Dict[str, Any]], Awaitable[None]]: ...
def email_verification_get_email_verification_url(recipe: ThirdPartyRecipe, get_email_verification_url: Callable[[User, Any], Awaitable[str]]) -> Callable[[EmailVerificationUser, Any], Awaitable[str]]: ...
def validate_and_normalise_email_verification_config(recipe: ThirdPartyRecipe, config: Union[InputEmailVerificationConfig, None], override: InputOverrideConfig) -> ParentRecipeEmailVerificationConfig: ...

class InputOverrideConfig:
    functions: Any
    apis: Any
    email_verification_feature: Any
    def __init__(self, functions: Union[Callable[[RecipeInterface], RecipeInterface], None] = ..., apis: Union[Callable[[APIInterface], APIInterface], None] = ..., email_verification_feature: Union[EmailVerificationOverrideConfig, None] = ...) -> None: ...

class OverrideConfig:
    functions: Any
    apis: Any
    def __init__(self, functions: Union[Callable[[RecipeInterface], RecipeInterface], None] = ..., apis: Union[Callable[[APIInterface], APIInterface], None] = ...) -> None: ...

class ThirdPartyConfig:
    sign_in_and_up_feature: Any
    email_verification_feature: Any
    override: Any
    def __init__(self, sign_in_and_up_feature: SignInAndUpFeature, email_verification_feature: ParentRecipeEmailVerificationConfig, override: OverrideConfig) -> None: ...

def validate_and_normalise_user_input(recipe: ThirdPartyRecipe, sign_in_and_up_feature: SignInAndUpFeature, email_verification_feature: Union[InputEmailVerificationConfig, None] = ..., override: Union[InputOverrideConfig, None] = ...) -> ThirdPartyConfig: ...
def find_right_provider(providers: List[Provider], third_party_id: str, client_id: Union[str, None]) -> Union[Provider, None]: ...
def verify_id_token_from_jwks_endpoint(id_token: str, jwks_uri: str, audience: str, issuers: List[str]) -> Dict[str, Any]: ...
