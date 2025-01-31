from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingGroupsIdCompaniesEndpoint import (
    MarketingGroupsIdCompaniesEndpoint,
)
from pyconnectwise.endpoints.manage.MarketingGroupsIdContactsEndpoint import (
    MarketingGroupsIdContactsEndpoint,
)
from pyconnectwise.endpoints.manage.MarketingGroupsIdInfoEndpoint import (
    MarketingGroupsIdInfoEndpoint,
)
from pyconnectwise.endpoints.manage.MarketingGroupsIdUsagesEndpoint import (
    MarketingGroupsIdUsagesEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import Group
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class MarketingGroupsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[Group, ConnectWiseManageRequestParams],
    IPuttable[Group, ConnectWiseManageRequestParams],
    IPatchable[Group, ConnectWiseManageRequestParams],
    IPaginateable[Group, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, Group)
        IPuttable.__init__(self, Group)
        IPatchable.__init__(self, Group)
        IPaginateable.__init__(self, Group)

        self.usages = self._register_child_endpoint(
            MarketingGroupsIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.companies = self._register_child_endpoint(
            MarketingGroupsIdCompaniesEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            MarketingGroupsIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.contacts = self._register_child_endpoint(
            MarketingGroupsIdContactsEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[Group]:
        """
        Performs a GET request against the /marketing/groups/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Group]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Group,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Group:
        """
        Performs a GET request against the /marketing/groups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Group: The parsed response data.
        """
        return self._parse_one(
            Group, super()._make_request("GET", data=data, params=params).json()
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /marketing/groups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Group:
        """
        Performs a PUT request against the /marketing/groups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Group: The parsed response data.
        """
        return self._parse_one(
            Group, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Group:
        """
        Performs a PATCH request against the /marketing/groups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Group: The parsed response data.
        """
        return self._parse_one(
            Group, super()._make_request("PATCH", data=data, params=params).json()
        )
