from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from enum import Enum
class Source(str, Enum):
    NONE = 'NONE'
    Member = 'Member'
    API = 'API'
    Workflow = 'Workflow'
    Portal = 'Portal'
    Mobile = 'Mobile'
    Network = 'Network'
    EmailConnector = 'EmailConnector'
    MassMaintenance = 'MassMaintenance'
    Application = 'Application'
    SystemAPI = 'SystemAPI'
    Conversion = 'Conversion'
class ExpenseEntryAuditModelType(str, Enum):
    Activity = 'Activity'
    CloseDate = 'CloseDate'
    Company = 'Company'
    Contact = 'Contact'
    Conversion = 'Conversion'
    Document = 'Document'
    Forecast = 'Forecast'
    Note = 'Note'
    Notes = 'Notes'
    Opportunity = 'Opportunity'
    Products = 'Products'
    Stage = 'Stage'
    Status = 'Status'
    Surveys = 'Surveys'
    Team = 'Team'
    Tracks = 'Tracks'
    Configuration = 'Configuration'
    ConfigurationQuestions = 'ConfigurationQuestions'
    DeviceBackupDetails = 'DeviceBackupDetails'
    Tickets = 'Tickets'
    Subject = 'Subject'
    ActivityOverview = 'ActivityOverview'
    Schedule = 'Schedule'
    Resources = 'Resources'
    ExpenseEntry = 'ExpenseEntry'
    Member = 'Member'
    Date = 'Date'
    Classification = 'Classification'
    Amount = 'Amount'
    ExpenseType = 'ExpenseType'
    WorkType = 'WorkType'
    WorkRole = 'WorkRole'
    Mileage = 'Mileage'
    Billing = 'Billing'
    ExpenseHeader = 'ExpenseHeader'
    Project = 'Project'
    TimeEntry = 'TimeEntry'
    TicketStatus = 'TicketStatus'
    DateTime = 'DateTime'
    DeductHours = 'DeductHours'
    ActualHours = 'ActualHours'
    Invoice = 'Invoice'
    CompanyFinance = 'CompanyFinance'
    Billable = 'Billable'
    SalesOrder = 'SalesOrder'
    Shipping = 'Shipping'
    Profile = 'Profile'
    Group = 'Group'
    GroupContact = 'GroupContact'
    GroupCompany = 'GroupCompany'
    Options = 'Options'
    Site = 'Site'
    Agreement = 'Agreement'
    Addition = 'Addition'
    Adjustment = 'Adjustment'
    API = 'API'
    ProjectFinance = 'ProjectFinance'
    CompanyProfile = 'CompanyProfile'
    CompanyTeam = 'CompanyTeam'
    CompanyMgmt = 'CompanyMgmt'
    InvoiceTotal = 'InvoiceTotal'
    BillingInformation = 'BillingInformation'
    ShippingInformation = 'ShippingInformation'
    BillingStatus = 'BillingStatus'
    Location = 'Location'
    Department = 'Department'
    Territory = 'Territory'
    Payment = 'Payment'
    Credit = 'Credit'
    SubcontractorInformation = 'SubcontractorInformation'
    InvoicingParameters = 'InvoicingParameters'
    ApplicationParameters = 'ApplicationParameters'
    Finance = 'Finance'
    Invoicing = 'Invoicing'
    Email = 'Email'
    Batching = 'Batching'
    KnowledgeBase = 'KnowledgeBase'
    KbArticle = 'KbArticle'
    KnowledgeBaseApproval = 'KnowledgeBaseApproval'
    KnowledgeBaseTicket = 'KnowledgeBaseTicket'
    ManageNetwork = 'ManageNetwork'
    Tasks = 'Tasks'
    CustomField = 'CustomField'
    ScreenConnect = 'ScreenConnect'
    SLA = 'SLA'
    Ticket = 'Ticket'
    Workflow = 'Workflow'
    Record = 'Record'
    CombinedTickets = 'CombinedTickets'
    Template = 'Template'
    PurchaseOrder = 'PurchaseOrder'
    Meeting = 'Meeting'
    RmaOverview = 'RmaOverview'
    ReturnedBy = 'ReturnedBy'
    PurchasedFromVendor = 'PurchasedFromVendor'
    WarrantyVendor = 'WarrantyVendor'
    RepairVendor = 'RepairVendor'
    AdditionalDetails = 'AdditionalDetails'
    TicketTemplate = 'TicketTemplate'
    AutoGeneration = 'AutoGeneration'
    TimeInternalNote = 'TimeInternalNote'
    TimeDiscussion = 'TimeDiscussion'
    TimeInternal = 'TimeInternal'
    TimeResolution = 'TimeResolution'

class ExpenseEntryAuditModel(ConnectWiseModel):
    id: int
    member: MemberReferenceModel
    source: Source
    type: ExpenseEntryAuditModelType
    message: str
    old_value: str
    new_value: str
    value: str
    _info: dict[str, str]