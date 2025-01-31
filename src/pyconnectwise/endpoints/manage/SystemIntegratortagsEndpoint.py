from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemIntegratortagsCountEndpoint import (
    SystemIntegratortagsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemIntegratortagsIdEndpoint import (
    SystemIntegratortagsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import IntegratorTag
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemIntegratortagsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[IntegratorTag], ConnectWiseManageRequestParams],
    IPostable[IntegratorTag, ConnectWiseManageRequestParams],
    IPaginateable[IntegratorTag, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "integratorTags", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[IntegratorTag])
        IPostable.__init__(self, IntegratorTag)
        IPaginateable.__init__(self, IntegratorTag)

        self.count = self._register_child_endpoint(
            SystemIntegratortagsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemIntegratortagsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SystemIntegratortagsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemIntegratortagsIdEndpoint: The initialized SystemIntegratortagsIdEndpoint object.
        """
        child = SystemIntegratortagsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[IntegratorTag]:
        """
        Performs a GET request against the /system/integratorTags endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[IntegratorTag]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            IntegratorTag,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[IntegratorTag]:
        """
        Performs a GET request against the /system/integratorTags endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[IntegratorTag]: The parsed response data.
        """
        return self._parse_many(
            IntegratorTag, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> IntegratorTag:
        """
        Performs a POST request against the /system/integratorTags endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            IntegratorTag: The parsed response data.
        """
        return self._parse_one(
            IntegratorTag,
            super()._make_request("POST", data=data, params=params).json(),
        )
