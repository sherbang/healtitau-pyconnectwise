from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class ServiceInfoModel(ConnectWiseModel):
    id: int
    header_color: str
    member_color: str
    contact_color: str
    unknown_color: str
    _info: dict[str, str]