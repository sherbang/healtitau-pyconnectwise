from pyconnectwise.endpoints.automate.ClientsIdEndpoint import ClientsIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.automate import LabTechClient
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class ClientsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechClient], ConnectWiseAutomateRequestParams],
    IPostable[LabTechClient, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechClient, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "Clients", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechClient])
        IPostable.__init__(self, LabTechClient)
        IPaginateable.__init__(self, LabTechClient)

    def id(self, id: int) -> ClientsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ClientsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ClientsIdEndpoint: The initialized ClientsIdEndpoint object.
        """
        child = ClientsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechClient]:
        """
        Performs a GET request against the /Clients endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechClient]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechClient,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechClient]:
        """
        Performs a GET request against the /Clients endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechClient]: The parsed response data.
        """
        return self._parse_many(
            LabTechClient, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechClient:
        """
        Performs a POST request against the /Clients endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechClient: The parsed response data.
        """
        return self._parse_one(
            LabTechClient,
            super()._make_request("POST", data=data, params=params).json(),
        )
