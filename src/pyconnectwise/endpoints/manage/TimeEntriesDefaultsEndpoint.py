from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPostable,
)
from pyconnectwise.models.manage import TimeEntry
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class TimeEntriesDefaultsEndpoint(
    ConnectWiseEndpoint, IPostable[TimeEntry, ConnectWiseManageRequestParams]
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "defaults", parent_endpoint=parent_endpoint
        )
        IPostable.__init__(self, TimeEntry)

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> TimeEntry:
        """
        Performs a POST request against the /time/entries/defaults endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TimeEntry: The parsed response data.
        """
        return self._parse_one(
            TimeEntry, super()._make_request("POST", data=data, params=params).json()
        )
