from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.automate import AutomateMaintenanceWindowDefinition
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class MaintenancewindowdefinitionsEndpoint(
    ConnectWiseEndpoint,
    IGettable[
        list[AutomateMaintenanceWindowDefinition], ConnectWiseAutomateRequestParams
    ],
    IPaginateable[
        AutomateMaintenanceWindowDefinition, ConnectWiseAutomateRequestParams
    ],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self,
            client,
            "Maintenancewindowdefinitions",
            parent_endpoint=parent_endpoint,
        )
        IGettable.__init__(self, list[AutomateMaintenanceWindowDefinition])
        IPaginateable.__init__(self, AutomateMaintenanceWindowDefinition)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[AutomateMaintenanceWindowDefinition]:
        """
        Performs a GET request against the /Maintenancewindowdefinitions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AutomateMaintenanceWindowDefinition]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AutomateMaintenanceWindowDefinition,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[AutomateMaintenanceWindowDefinition]:
        """
        Performs a GET request against the /Maintenancewindowdefinitions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AutomateMaintenanceWindowDefinition]: The parsed response data.
        """
        return self._parse_many(
            AutomateMaintenanceWindowDefinition,
            super()._make_request("GET", data=data, params=params).json(),
        )
