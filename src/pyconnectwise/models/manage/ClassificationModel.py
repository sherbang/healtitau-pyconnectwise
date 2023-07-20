from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class ClassificationModel(ConnectWiseModel):
    id: int
    name: str
    multiplier: float
    default_flag: bool
    company_flag: bool
    employee_flag: bool
    _info: dict[str, str]