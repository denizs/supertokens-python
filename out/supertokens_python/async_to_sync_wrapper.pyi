from typing import Any, Coroutine

def check_event_loop() -> None: ...
def sync(co: Coroutine[Any, Any, _T]) -> _T: ...
