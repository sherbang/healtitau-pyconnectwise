from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectStatusesIdInfoEndpoint import (
    ProjectStatusesIdInfoEndpoint,
)
from pyconnectwise.endpoints.manage.ProjectStatusesIdUsagesEndpoint import (
    ProjectStatusesIdUsagesEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import ProjectStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ProjectStatusesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[ProjectStatus, ConnectWiseManageRequestParams],
    IPuttable[ProjectStatus, ConnectWiseManageRequestParams],
    IPatchable[ProjectStatus, ConnectWiseManageRequestParams],
    IPaginateable[ProjectStatus, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, ProjectStatus)
        IPuttable.__init__(self, ProjectStatus)
        IPatchable.__init__(self, ProjectStatus)
        IPaginateable.__init__(self, ProjectStatus)

        self.usages = self._register_child_endpoint(
            ProjectStatusesIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            ProjectStatusesIdInfoEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ProjectStatus]:
        """
        Performs a GET request against the /project/statuses/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectStatus]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ProjectStatus,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ProjectStatus:
        """
        Performs a GET request against the /project/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectStatus: The parsed response data.
        """
        return self._parse_one(
            ProjectStatus, super()._make_request("GET", data=data, params=params).json()
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /project/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ProjectStatus:
        """
        Performs a PUT request against the /project/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectStatus: The parsed response data.
        """
        return self._parse_one(
            ProjectStatus, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ProjectStatus:
        """
        Performs a PATCH request against the /project/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectStatus: The parsed response data.
        """
        return self._parse_one(
            ProjectStatus,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
