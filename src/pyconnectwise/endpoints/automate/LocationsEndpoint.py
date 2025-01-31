from pyconnectwise.endpoints.automate.LocationsIdEndpoint import LocationsIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.automate import AutomateLocation, LabTechLocation
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class LocationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AutomateLocation], ConnectWiseAutomateRequestParams],
    IPostable[LabTechLocation, ConnectWiseAutomateRequestParams],
    IPaginateable[AutomateLocation, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "Locations", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[AutomateLocation])
        IPostable.__init__(self, LabTechLocation)
        IPaginateable.__init__(self, AutomateLocation)

    def id(self, id: int) -> LocationsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized LocationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            LocationsIdEndpoint: The initialized LocationsIdEndpoint object.
        """
        child = LocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[AutomateLocation]:
        """
        Performs a GET request against the /Locations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AutomateLocation]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AutomateLocation,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[AutomateLocation]:
        """
        Performs a GET request against the /Locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AutomateLocation]: The parsed response data.
        """
        return self._parse_many(
            AutomateLocation,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechLocation:
        """
        Performs a POST request against the /Locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechLocation: The parsed response data.
        """
        return self._parse_one(
            LabTechLocation,
            super()._make_request("POST", data=data, params=params).json(),
        )
