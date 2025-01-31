from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemAuthanvilsCountEndpoint import (
    SystemAuthanvilsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemAuthanvilsIdEndpoint import (
    SystemAuthanvilsIdEndpoint,
)
from pyconnectwise.endpoints.manage.SystemAuthanvilsTestconnectionEndpoint import (
    SystemAuthanvilsTestconnectionEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import AuthAnvil
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemAuthanvilsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AuthAnvil], ConnectWiseManageRequestParams],
    IPaginateable[AuthAnvil, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "authAnvils", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[AuthAnvil])
        IPaginateable.__init__(self, AuthAnvil)

        self.count = self._register_child_endpoint(
            SystemAuthanvilsCountEndpoint(client, parent_endpoint=self)
        )
        self.test_connection = self._register_child_endpoint(
            SystemAuthanvilsTestconnectionEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemAuthanvilsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SystemAuthanvilsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemAuthanvilsIdEndpoint: The initialized SystemAuthanvilsIdEndpoint object.
        """
        child = SystemAuthanvilsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[AuthAnvil]:
        """
        Performs a GET request against the /system/authAnvils endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AuthAnvil]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AuthAnvil,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[AuthAnvil]:
        """
        Performs a GET request against the /system/authAnvils endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AuthAnvil]: The parsed response data.
        """
        return self._parse_many(
            AuthAnvil, super()._make_request("GET", data=data, params=params).json()
        )
