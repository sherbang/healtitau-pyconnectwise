from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemConnectwisehostedsetupsCountEndpoint import (
    SystemConnectwisehostedsetupsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemConnectwisehostedsetupsIdEndpoint import (
    SystemConnectwisehostedsetupsIdEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import ConnectWiseHostedSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemConnectwisehostedsetupsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ConnectWiseHostedSetup], ConnectWiseManageRequestParams],
    IPostable[ConnectWiseHostedSetup, ConnectWiseManageRequestParams],
    IPaginateable[ConnectWiseHostedSetup, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "connectwisehostedsetups", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ConnectWiseHostedSetup])
        IPostable.__init__(self, ConnectWiseHostedSetup)
        IPaginateable.__init__(self, ConnectWiseHostedSetup)

        self.count = self._register_child_endpoint(
            SystemConnectwisehostedsetupsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> SystemConnectwisehostedsetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemConnectwisehostedsetupsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemConnectwisehostedsetupsIdEndpoint: The initialized SystemConnectwisehostedsetupsIdEndpoint object.
        """
        child = SystemConnectwisehostedsetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ConnectWiseHostedSetup]:
        """
        Performs a GET request against the /system/connectwisehostedsetups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ConnectWiseHostedSetup]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ConnectWiseHostedSetup, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ConnectWiseHostedSetup]:
        """
        Performs a GET request against the /system/connectwisehostedsetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ConnectWiseHostedSetup]: The parsed response data.
        """
        return self._parse_many(ConnectWiseHostedSetup, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ConnectWiseHostedSetup:
        """
        Performs a POST request against the /system/connectwisehostedsetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ConnectWiseHostedSetup: The parsed response data.
        """
        return self._parse_one(ConnectWiseHostedSetup, super()._make_request("POST", data=data, params=params).json())
