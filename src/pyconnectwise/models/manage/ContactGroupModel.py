from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.GroupReferenceModel import GroupReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel

class ContactGroupModel(ConnectWiseModel):
    id: int
    group: GroupReferenceModel
    contact: ContactReferenceModel
    description: str
    unsubscribe_flag: bool
    company_unsubcribed_email_message: str
    company_group_unsubscribed_email_message: str
    contact_unsubscribed_email_message: str
    contact_group_unsubscribed_email_message: str
    _info: dict[str, str]