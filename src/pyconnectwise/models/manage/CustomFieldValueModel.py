from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class CustomFieldValueModelType(str, Enum):
    TextArea = 'TextArea'
    Button = 'Button'
    Currency = 'Currency'
    Date = 'Date'
    Hyperlink = 'Hyperlink'
    IPAddress = 'IPAddress'
    Checkbox = 'Checkbox'
    Number = 'Number'
    Percent = 'Percent'
    Text = 'Text'
    Password = 'Password'
class EntryMethod(str, Enum):
    Date = 'Date'
    EntryField = 'EntryField'
    List = 'List'
    Option = 'Option'

class CustomFieldValueModel(ConnectWiseModel):
    id: int
    caption: str
    type: CustomFieldValueModelType
    entry_method: EntryMethod
    number_of_decimals: int
    value: Any