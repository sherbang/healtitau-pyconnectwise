from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.NotificationRecipientReferenceModel import NotificationRecipientReferenceModel
from pyconnectwise.models.manage.PurchaseOrderStatusReferenceModel import PurchaseOrderStatusReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel

class PurchaseOrderStatusNotificationModel(ConnectWiseModel):
    id: int
    notify_who: NotificationRecipientReferenceModel
    status: PurchaseOrderStatusReferenceModel
    member: MemberReferenceModel
    email: str
    workflow_step: int
    _info: dict[str, str]