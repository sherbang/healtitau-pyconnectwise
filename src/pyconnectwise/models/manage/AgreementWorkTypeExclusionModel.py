from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel

class AgreementWorkTypeExclusionModel(ConnectWiseModel):
    id: int
    work_type: WorkTypeReferenceModel
    agreement_id: int
    _info: dict[str, str]