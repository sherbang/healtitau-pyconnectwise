from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsEndpoint import (
    FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPatchable, IPuttable
from pyconnectwise.models.manage import TaxCodeXRef
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams, PatchRequestData

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class FinanceTaxcodesIdTaxcodexrefsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[TaxCodeXRef, ConnectWiseManageRequestParams],
    IPatchable[TaxCodeXRef, ConnectWiseManageRequestParams],
    IPuttable[TaxCodeXRef, ConnectWiseManageRequestParams],
    IPaginateable[TaxCodeXRef, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, TaxCodeXRef)
        IPatchable.__init__(self, TaxCodeXRef)
        IPuttable.__init__(self, TaxCodeXRef)
        IPaginateable.__init__(self, TaxCodeXRef)

        self.taxable_x_ref_levels = self._register_child_endpoint(
            FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[TaxCodeXRef]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/taxCodeXRefs/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxCodeXRef]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), TaxCodeXRef, self, page, page_size, params
        )

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /finance/taxCodes/{id}/taxCodeXRefs/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> TaxCodeXRef:
        """
        Performs a GET request against the /finance/taxCodes/{id}/taxCodeXRefs/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxCodeXRef: The parsed response data.
        """
        return self._parse_one(TaxCodeXRef, super()._make_request("GET", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> TaxCodeXRef:
        """
        Performs a PATCH request against the /finance/taxCodes/{id}/taxCodeXRefs/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxCodeXRef: The parsed response data.
        """
        return self._parse_one(TaxCodeXRef, super()._make_request("PATCH", data=data, params=params).json())

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> TaxCodeXRef:
        """
        Performs a PUT request against the /finance/taxCodes/{id}/taxCodeXRefs/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxCodeXRef: The parsed response data.
        """
        return self._parse_one(TaxCodeXRef, super()._make_request("PUT", data=data, params=params).json())
