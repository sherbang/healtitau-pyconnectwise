from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import PortalConfigurationPaymentProcessor
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class CompanyPortalconfigurationsInvoicesetupPaymentprocessorsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[PortalConfigurationPaymentProcessor, ConnectWiseManageRequestParams],
    IPaginateable[PortalConfigurationPaymentProcessor, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, PortalConfigurationPaymentProcessor)
        IPaginateable.__init__(self, PortalConfigurationPaymentProcessor)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[PortalConfigurationPaymentProcessor]:
        """
        Performs a GET request against the /company/portalConfigurations/invoiceSetup/paymentProcessors/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalConfigurationPaymentProcessor]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            PortalConfigurationPaymentProcessor,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PortalConfigurationPaymentProcessor:
        """
        Performs a GET request against the /company/portalConfigurations/invoiceSetup/paymentProcessors/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationPaymentProcessor: The parsed response data.
        """
        return self._parse_one(
            PortalConfigurationPaymentProcessor,
            super()._make_request("GET", data=data, params=params).json(),
        )
