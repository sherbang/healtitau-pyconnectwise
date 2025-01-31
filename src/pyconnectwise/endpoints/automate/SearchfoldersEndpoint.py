from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.automate import LabTechSearchFolder
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class SearchfoldersEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechSearchFolder], ConnectWiseAutomateRequestParams],
    IPostable[LabTechSearchFolder, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechSearchFolder, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "Searchfolders", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechSearchFolder])
        IPostable.__init__(self, LabTechSearchFolder)
        IPaginateable.__init__(self, LabTechSearchFolder)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechSearchFolder]:
        """
        Performs a GET request against the /Searchfolders endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechSearchFolder]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechSearchFolder,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechSearchFolder]:
        """
        Performs a GET request against the /Searchfolders endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechSearchFolder]: The parsed response data.
        """
        return self._parse_many(
            LabTechSearchFolder,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechSearchFolder:
        """
        Performs a POST request against the /Searchfolders endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechSearchFolder: The parsed response data.
        """
        return self._parse_one(
            LabTechSearchFolder,
            super()._make_request("POST", data=data, params=params).json(),
        )
