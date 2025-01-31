from pyconnectwise.endpoints.automate.MonitorsIdEndpoint import MonitorsIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class MonitorsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "Monitors", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> MonitorsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized MonitorsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            MonitorsIdEndpoint: The initialized MonitorsIdEndpoint object.
        """
        child = MonitorsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
