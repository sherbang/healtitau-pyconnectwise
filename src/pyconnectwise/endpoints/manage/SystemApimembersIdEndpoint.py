from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import ApiMember
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SystemApimembersIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[ApiMember, ConnectWiseManageRequestParams],
    IPuttable[ApiMember, ConnectWiseManageRequestParams],
    IPatchable[ApiMember, ConnectWiseManageRequestParams],
    IPaginateable[ApiMember, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, ApiMember)
        IPuttable.__init__(self, ApiMember)
        IPatchable.__init__(self, ApiMember)
        IPaginateable.__init__(self, ApiMember)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ApiMember]:
        """
        Performs a GET request against the /system/apiMembers/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ApiMember]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ApiMember,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ApiMember:
        """
        Performs a GET request against the /system/apiMembers/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ApiMember: The parsed response data.
        """
        return self._parse_one(
            ApiMember, super()._make_request("GET", data=data, params=params).json()
        )

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ApiMember:
        """
        Performs a PUT request against the /system/apiMembers/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ApiMember: The parsed response data.
        """
        return self._parse_one(
            ApiMember, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ApiMember:
        """
        Performs a PATCH request against the /system/apiMembers/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ApiMember: The parsed response data.
        """
        return self._parse_one(
            ApiMember, super()._make_request("PATCH", data=data, params=params).json()
        )
