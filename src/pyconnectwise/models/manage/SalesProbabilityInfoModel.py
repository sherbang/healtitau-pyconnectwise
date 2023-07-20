from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class SalesProbabilityInfoModel(ConnectWiseModel):
    id: int
    probability: int
    _info: dict[str, str]