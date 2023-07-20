from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.UserDefinedFieldReferenceModel import UserDefinedFieldReferenceModel

class WorkflowTriggerOptionModel(ConnectWiseModel):
    value: str
    name: str
    custom_field: UserDefinedFieldReferenceModel
    _info: dict[str, str]