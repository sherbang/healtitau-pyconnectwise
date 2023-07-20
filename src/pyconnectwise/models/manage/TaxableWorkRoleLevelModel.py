from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.TaxCodeLevelReferenceModel import TaxCodeLevelReferenceModel

class TaxableWorkRoleLevelModel(ConnectWiseModel):
    id: int
    tax_code_level: TaxCodeLevelReferenceModel
    _info: dict[str, str]