import json, os

from typing import Union

def join_path(paths: list) -> str:
    return os.sep.join(paths)

def json_pretty(content: Union[bytes, dict, str], indent: int = 4) -> str:
    if not isinstance(content, dict):
        content = json.loads(content)
    return json.dumps(content, indent=indent)
