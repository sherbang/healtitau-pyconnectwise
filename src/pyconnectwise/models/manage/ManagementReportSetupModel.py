from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class ManagementReportSetupModel(ConnectWiseModel):
    id: int
    scheduled_report_disabled_flag: bool
    _info: dict[str, str]