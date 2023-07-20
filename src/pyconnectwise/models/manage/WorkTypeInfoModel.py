from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class WorkTypeInfoModel(ConnectWiseModel):
    id: int
    name: str
    default_flag: bool
    inactive_flag: bool
    activity_default_flag: bool
    _info: dict[str, str]