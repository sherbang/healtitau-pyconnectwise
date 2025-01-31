from pyconnectwise.endpoints.automate.GroupsIdEndpoint import GroupsIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.automate import LabTechGroup
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class GroupsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechGroup], ConnectWiseAutomateRequestParams],
    IPostable[LabTechGroup, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechGroup, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "Groups", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechGroup])
        IPostable.__init__(self, LabTechGroup)
        IPaginateable.__init__(self, LabTechGroup)

    def id(self, id: int) -> GroupsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized GroupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            GroupsIdEndpoint: The initialized GroupsIdEndpoint object.
        """
        child = GroupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechGroup]:
        """
        Performs a GET request against the /Groups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechGroup]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechGroup,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechGroup]:
        """
        Performs a GET request against the /Groups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechGroup]: The parsed response data.
        """
        return self._parse_many(
            LabTechGroup, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechGroup:
        """
        Performs a POST request against the /Groups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechGroup: The parsed response data.
        """
        return self._parse_one(
            LabTechGroup, super()._make_request("POST", data=data, params=params).json()
        )
