from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel

class EPayConfigurationModel(ConnectWiseModel):
    id: int
    location: SystemLocationReferenceModel
    currency: CurrencyReferenceModel
    url: str
    store_identifier: str
    encryption_key: str
    initialization_vector: str
    _info: dict[str, str]