from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import PurchaseOrderLineItem
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ProcurementPurchaseordersIdLineitemsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[PurchaseOrderLineItem, ConnectWiseManageRequestParams],
    IPuttable[PurchaseOrderLineItem, ConnectWiseManageRequestParams],
    IPatchable[PurchaseOrderLineItem, ConnectWiseManageRequestParams],
    IPaginateable[PurchaseOrderLineItem, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, PurchaseOrderLineItem)
        IPuttable.__init__(self, PurchaseOrderLineItem)
        IPatchable.__init__(self, PurchaseOrderLineItem)
        IPaginateable.__init__(self, PurchaseOrderLineItem)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[PurchaseOrderLineItem]:
        """
        Performs a GET request against the /procurement/purchaseorders/{id}/lineitems/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PurchaseOrderLineItem]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            PurchaseOrderLineItem,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PurchaseOrderLineItem:
        """
        Performs a GET request against the /procurement/purchaseorders/{id}/lineitems/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PurchaseOrderLineItem: The parsed response data.
        """
        return self._parse_one(
            PurchaseOrderLineItem,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PurchaseOrderLineItem:
        """
        Performs a PUT request against the /procurement/purchaseorders/{id}/lineitems/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PurchaseOrderLineItem: The parsed response data.
        """
        return self._parse_one(
            PurchaseOrderLineItem,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PurchaseOrderLineItem:
        """
        Performs a PATCH request against the /procurement/purchaseorders/{id}/lineitems/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PurchaseOrderLineItem: The parsed response data.
        """
        return self._parse_one(
            PurchaseOrderLineItem,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
