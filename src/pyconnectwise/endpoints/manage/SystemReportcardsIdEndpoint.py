from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemReportcardsIdDetailsEndpoint import (
    SystemReportcardsIdDetailsEndpoint,
)
from pyconnectwise.endpoints.manage.SystemReportcardsIdInfoEndpoint import (
    SystemReportcardsIdInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import ReportCard
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SystemReportcardsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[ReportCard, ConnectWiseManageRequestParams],
    IPuttable[ReportCard, ConnectWiseManageRequestParams],
    IPatchable[ReportCard, ConnectWiseManageRequestParams],
    IPaginateable[ReportCard, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, ReportCard)
        IPuttable.__init__(self, ReportCard)
        IPatchable.__init__(self, ReportCard)
        IPaginateable.__init__(self, ReportCard)

        self.details = self._register_child_endpoint(
            SystemReportcardsIdDetailsEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            SystemReportcardsIdInfoEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ReportCard]:
        """
        Performs a GET request against the /system/reportCards/{id} endpoint and returns an initialized PaginatedResponse object.

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
    ) -> ReportCard:
        """
        Performs a GET request against the /system/reportCards/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ReportCard: The parsed response data.
        """
        return self._parse_one(
            ReportCard, super()._make_request("GET", data=data, params=params).json()
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /system/reportCards/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ReportCard:
        """
        Performs a PUT request against the /system/reportCards/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ReportCard: The parsed response data.
        """
        return self._parse_one(
            ReportCard, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ReportCard:
        """
        Performs a PATCH request against the /system/reportCards/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ReportCard: The parsed response data.
        """
        return self._parse_one(
            ReportCard, super()._make_request("PATCH", data=data, params=params).json()
        )
