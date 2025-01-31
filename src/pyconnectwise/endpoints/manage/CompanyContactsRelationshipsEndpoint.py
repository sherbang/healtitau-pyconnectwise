from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsRelationshipsCountEndpoint import (
    CompanyContactsRelationshipsCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyContactsRelationshipsIdEndpoint import (
    CompanyContactsRelationshipsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import ContactRelationship
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class CompanyContactsRelationshipsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ContactRelationship], ConnectWiseManageRequestParams],
    IPostable[ContactRelationship, ConnectWiseManageRequestParams],
    IPaginateable[ContactRelationship, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "relationships", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ContactRelationship])
        IPostable.__init__(self, ContactRelationship)
        IPaginateable.__init__(self, ContactRelationship)

        self.count = self._register_child_endpoint(
            CompanyContactsRelationshipsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyContactsRelationshipsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsRelationshipsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactsRelationshipsIdEndpoint: The initialized CompanyContactsRelationshipsIdEndpoint object.
        """
        child = CompanyContactsRelationshipsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ContactRelationship]:
        """
        Performs a GET request against the /company/contacts/relationships endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactRelationship]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ContactRelationship,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ContactRelationship]:
        """
        Performs a GET request against the /company/contacts/relationships endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactRelationship]: The parsed response data.
        """
        return self._parse_many(
            ContactRelationship,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ContactRelationship:
        """
        Performs a POST request against the /company/contacts/relationships endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactRelationship: The parsed response data.
        """
        return self._parse_one(
            ContactRelationship,
            super()._make_request("POST", data=data, params=params).json(),
        )
