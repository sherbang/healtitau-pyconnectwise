from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemInfoStandardnotesCountEndpoint import (
    SystemInfoStandardnotesCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemInfoStandardnotesIdEndpoint import (
    SystemInfoStandardnotesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import StandardNoteInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemInfoStandardnotesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[StandardNoteInfo], ConnectWiseManageRequestParams],
    IPaginateable[StandardNoteInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "standardNotes", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[StandardNoteInfo])
        IPaginateable.__init__(self, StandardNoteInfo)

        self.count = self._register_child_endpoint(
            SystemInfoStandardnotesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemInfoStandardnotesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SystemInfoStandardnotesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemInfoStandardnotesIdEndpoint: The initialized SystemInfoStandardnotesIdEndpoint object.
        """
        child = SystemInfoStandardnotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[StandardNoteInfo]:
        """
        Performs a GET request against the /system/info/standardNotes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[StandardNoteInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            StandardNoteInfo,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[StandardNoteInfo]:
        """
        Performs a GET request against the /system/info/standardNotes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[StandardNoteInfo]: The parsed response data.
        """
        return self._parse_many(
            StandardNoteInfo,
            super()._make_request("GET", data=data, params=params).json(),
        )
