from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import SuccessResponse
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemManagementnetworksecuritiesIdTestcredentialsEndpoint(
    ConnectWiseEndpoint,
    IGettable[SuccessResponse, ConnectWiseManageRequestParams],
    IPaginateable[SuccessResponse, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "testCredentials", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, SuccessResponse)
        IPaginateable.__init__(self, SuccessResponse)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[SuccessResponse]:
        """
        Performs a GET request against the /system/managementNetworkSecurities/{id}/testCredentials endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SuccessResponse]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            SuccessResponse,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> SuccessResponse:
        """
        Performs a GET request against the /system/managementNetworkSecurities/{id}/testCredentials endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SuccessResponse: The parsed response data.
        """
        return self._parse_one(
            SuccessResponse,
            super()._make_request("GET", data=data, params=params).json(),
        )
