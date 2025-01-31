from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPuttable,
)
from pyconnectwise.models.manage import CompanyFinance
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class CompanyCompanyfinanceIdEndpoint(
    ConnectWiseEndpoint, IPuttable[CompanyFinance, ConnectWiseManageRequestParams]
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IPuttable.__init__(self, CompanyFinance)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> CompanyFinance:
        """
        Performs a PUT request against the /company/companyFinance/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyFinance: The parsed response data.
        """
        return self._parse_one(
            CompanyFinance,
            super()._make_request("PUT", data=data, params=params).json(),
        )
