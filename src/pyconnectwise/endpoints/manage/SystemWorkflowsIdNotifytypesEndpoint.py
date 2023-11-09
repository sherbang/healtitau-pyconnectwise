from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdNotifytypesCountEndpoint import (
    SystemWorkflowsIdNotifytypesCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemWorkflowsIdNotifytypesIdEndpoint import SystemWorkflowsIdNotifytypesIdEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdNotifytypesInfoEndpoint import (
    SystemWorkflowsIdNotifytypesInfoEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable
from pyconnectwise.models.manage import WorkflowNotifyType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemWorkflowsIdNotifytypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[WorkflowNotifyType], ConnectWiseManageRequestParams],
    IPaginateable[WorkflowNotifyType, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "notifyTypes", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[WorkflowNotifyType])
        IPaginateable.__init__(self, WorkflowNotifyType)

        self.count = self._register_child_endpoint(
            SystemWorkflowsIdNotifytypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            SystemWorkflowsIdNotifytypesInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> SystemWorkflowsIdNotifytypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowsIdNotifytypesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemWorkflowsIdNotifytypesIdEndpoint: The initialized SystemWorkflowsIdNotifytypesIdEndpoint object.
        """
        child = SystemWorkflowsIdNotifytypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[WorkflowNotifyType]:
        """
        Performs a GET request against the /system/workflows/{id}/notifyTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkflowNotifyType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), WorkflowNotifyType, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[WorkflowNotifyType]:
        """
        Performs a GET request against the /system/workflows/{id}/notifyTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkflowNotifyType]: The parsed response data.
        """
        return self._parse_many(WorkflowNotifyType, super()._make_request("GET", data=data, params=params).json())
