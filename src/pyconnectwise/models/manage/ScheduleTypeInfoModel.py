from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ChargeCodeReferenceModel import ChargeCodeReferenceModel
from pyconnectwise.models.manage.ServiceLocationReferenceModel import ServiceLocationReferenceModel

class ScheduleTypeInfoModel(ConnectWiseModel):
    id: int
    name: str
    identifier: str
    charge_code: ChargeCodeReferenceModel
    where: ServiceLocationReferenceModel
    system_flag: bool
    _info: dict[str, str]