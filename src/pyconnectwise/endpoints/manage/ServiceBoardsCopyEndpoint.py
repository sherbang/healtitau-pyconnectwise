from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPostable,
)
from pyconnectwise.models.manage import Board
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ServiceBoardsCopyEndpoint(
    ConnectWiseEndpoint, IPostable[Board, ConnectWiseManageRequestParams]
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "copy", parent_endpoint=parent_endpoint
        )
        IPostable.__init__(self, Board)

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Board:
        """
        Performs a POST request against the /service/boards/copy endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Board: The parsed response data.
        """
        return self._parse_one(
            Board, super()._make_request("POST", data=data, params=params).json()
        )
