from .constants import API_KEY_HEADER as API_KEY_HEADER, API_VERSION as API_VERSION, API_VERSION_HEADER as API_VERSION_HEADER, RID_KEY_HEADER as RID_KEY_HEADER, SUPPORTED_CDI_VERSIONS as SUPPORTED_CDI_VERSIONS
from .exceptions import raise_general_exception as raise_general_exception
from .normalised_url_path import NormalisedURLPath as NormalisedURLPath
from .process_state import AllowedProcessStates as AllowedProcessStates, ProcessState as ProcessState
from .supertokens import Host as Host
from .utils import find_max_version as find_max_version, is_4xx_error as is_4xx_error, is_5xx_error as is_5xx_error
from httpx import Response as Response
from typing import Any, Dict, List, Union

class Querier:
    def __init__(self, hosts: List[Host], rid_to_core: Union[None, str] = ...) -> None: ...
    @staticmethod
    def reset() -> None: ...
    @staticmethod
    def get_hosts_alive_for_testing(): ...
    async def get_api_version(self): ...
    @staticmethod
    def get_instance(rid_to_core: Union[str, None] = ...): ...
    @staticmethod
    def init(hosts: List[Host], api_key: Union[str, None] = ...): ...
    async def send_get_request(self, path: NormalisedURLPath, params: Union[Dict[str, Any], None] = ...): ...
    async def send_post_request(self, path: NormalisedURLPath, data: Union[Dict[str, Any], None] = ..., test: bool = ...): ...
    async def send_delete_request(self, path: NormalisedURLPath): ...
    async def send_put_request(self, path: NormalisedURLPath, data: Union[Dict[str, Any], None] = ...): ...
