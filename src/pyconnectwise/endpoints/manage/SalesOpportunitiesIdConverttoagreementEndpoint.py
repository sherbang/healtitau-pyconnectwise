from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPostable,
)
from pyconnectwise.models.manage import Agreement
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SalesOpportunitiesIdConverttoagreementEndpoint(
    ConnectWiseEndpoint, IPostable[Agreement, ConnectWiseManageRequestParams]
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "convertToAgreement", parent_endpoint=parent_endpoint
        )
        IPostable.__init__(self, Agreement)

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Agreement:
        """
        Performs a POST request against the /sales/opportunities/{id}/convertToAgreement endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Agreement: The parsed response data.
        """
        return self._parse_one(
            Agreement, super()._make_request("POST", data=data, params=params).json()
        )
