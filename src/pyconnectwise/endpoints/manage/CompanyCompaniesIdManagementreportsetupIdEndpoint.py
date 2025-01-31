from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import ManagementReportSetup
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class CompanyCompaniesIdManagementreportsetupIdEndpoint(
    ConnectWiseEndpoint,
    IPuttable[ManagementReportSetup, ConnectWiseManageRequestParams],
    IPatchable[ManagementReportSetup, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IPuttable.__init__(self, ManagementReportSetup)
        IPatchable.__init__(self, ManagementReportSetup)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ManagementReportSetup:
        """
        Performs a PUT request against the /company/companies/{id}/managementReportSetup/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagementReportSetup: The parsed response data.
        """
        return self._parse_one(
            ManagementReportSetup,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ManagementReportSetup:
        """
        Performs a PATCH request against the /company/companies/{id}/managementReportSetup/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagementReportSetup: The parsed response data.
        """
        return self._parse_one(
            ManagementReportSetup,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
