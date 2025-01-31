from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectProjecttypesCountEndpoint import (
    ProjectProjecttypesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProjectProjecttypesIdEndpoint import (
    ProjectProjecttypesIdEndpoint,
)
from pyconnectwise.endpoints.manage.ProjectProjecttypesInfoEndpoint import (
    ProjectProjecttypesInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import ProjectType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ProjectProjecttypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ProjectType], ConnectWiseManageRequestParams],
    IPostable[ProjectType, ConnectWiseManageRequestParams],
    IPaginateable[ProjectType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "projectTypes", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ProjectType])
        IPostable.__init__(self, ProjectType)
        IPaginateable.__init__(self, ProjectType)

        self.count = self._register_child_endpoint(
            ProjectProjecttypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            ProjectProjecttypesInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProjectProjecttypesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ProjectProjecttypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectProjecttypesIdEndpoint: The initialized ProjectProjecttypesIdEndpoint object.
        """
        child = ProjectProjecttypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ProjectType]:
        """
        Performs a GET request against the /project/projectTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ProjectType,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ProjectType]:
        """
        Performs a GET request against the /project/projectTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectType]: The parsed response data.
        """
        return self._parse_many(
            ProjectType, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ProjectType:
        """
        Performs a POST request against the /project/projectTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectType: The parsed response data.
        """
        return self._parse_one(
            ProjectType, super()._make_request("POST", data=data, params=params).json()
        )
