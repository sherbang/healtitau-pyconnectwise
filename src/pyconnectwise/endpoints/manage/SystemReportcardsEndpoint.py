from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemReportcardsCountEndpoint import (
    SystemReportcardsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemReportcardsIdEndpoint import (
    SystemReportcardsIdEndpoint,
)
from pyconnectwise.endpoints.manage.SystemReportcardsInfoEndpoint import (
    SystemReportcardsInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import ReportCard
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemReportcardsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ReportCard], ConnectWiseManageRequestParams],
    IPostable[ReportCard, ConnectWiseManageRequestParams],
    IPaginateable[ReportCard, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "reportCards", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ReportCard])
        IPostable.__init__(self, ReportCard)
        IPaginateable.__init__(self, ReportCard)

        self.count = self._register_child_endpoint(
            SystemReportcardsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            SystemReportcardsInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemReportcardsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SystemReportcardsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemReportcardsIdEndpoint: The initialized SystemReportcardsIdEndpoint object.
        """
        child = SystemReportcardsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ReportCard]:
        """
        Performs a GET request against the /system/reportCards endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ReportCard]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ReportCard,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ReportCard]:
        """
        Performs a GET request against the /system/reportCards endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ReportCard]: The parsed response data.
        """
        return self._parse_many(
            ReportCard, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ReportCard:
        """
        Performs a POST request against the /system/reportCards endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ReportCard: The parsed response data.
        """
        return self._parse_one(
            ReportCard, super()._make_request("POST", data=data, params=params).json()
        )
