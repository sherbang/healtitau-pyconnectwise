from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdTriggersIdOptionsCountEndpoint import (
    SystemWorkflowsIdTriggersIdOptionsCountEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import WorkflowTriggerOption
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemWorkflowsIdTriggersIdOptionsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[WorkflowTriggerOption], ConnectWiseManageRequestParams],
    IPaginateable[WorkflowTriggerOption, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "options", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[WorkflowTriggerOption])
        IPaginateable.__init__(self, WorkflowTriggerOption)

        self.count = self._register_child_endpoint(
            SystemWorkflowsIdTriggersIdOptionsCountEndpoint(
                client, parent_endpoint=self
            )
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[WorkflowTriggerOption]:
        """
        Performs a GET request against the /system/workflows/{id}/triggers/{id}/options endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkflowTriggerOption]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            WorkflowTriggerOption,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[WorkflowTriggerOption]:
        """
        Performs a GET request against the /system/workflows/{id}/triggers/{id}/options endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkflowTriggerOption]: The parsed response data.
        """
        return self._parse_many(
            WorkflowTriggerOption,
            super()._make_request("GET", data=data, params=params).json(),
        )
