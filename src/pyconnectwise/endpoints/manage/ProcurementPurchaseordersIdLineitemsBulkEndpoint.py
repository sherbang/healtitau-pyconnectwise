from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IPostable, IPuttable
from pyconnectwise.models.manage import BulkResult
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ProcurementPurchaseordersIdLineitemsBulkEndpoint(
    ConnectWiseEndpoint,
    IDeleteable[ConnectWiseManageRequestParams],
    IPostable[BulkResult, ConnectWiseManageRequestParams],
    IPuttable[BulkResult, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "bulk", parent_endpoint=parent_endpoint)
        IDeleteable.__init__(self, None)
        IPostable.__init__(self, BulkResult)
        IPuttable.__init__(self, BulkResult)

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> BulkResult:
        """
        Performs a DELETE request against the /procurement/purchaseorders/{id}/lineitems/bulk endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BulkResult: The parsed response data.
        """
        return self._parse_one(BulkResult, super()._make_request("DELETE", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> BulkResult:
        """
        Performs a POST request against the /procurement/purchaseorders/{id}/lineitems/bulk endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BulkResult: The parsed response data.
        """
        return self._parse_one(BulkResult, super()._make_request("POST", data=data, params=params).json())

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> BulkResult:
        """
        Performs a PUT request against the /procurement/purchaseorders/{id}/lineitems/bulk endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BulkResult: The parsed response data.
        """
        return self._parse_one(BulkResult, super()._make_request("PUT", data=data, params=params).json())
