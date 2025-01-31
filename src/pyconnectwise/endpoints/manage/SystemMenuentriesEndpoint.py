from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMenuentriesIdEndpoint import (
    SystemMenuentriesIdEndpoint,
)


class SystemMenuentriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "menuEntries", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> SystemMenuentriesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SystemMenuentriesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMenuentriesIdEndpoint: The initialized SystemMenuentriesIdEndpoint object.
        """
        child = SystemMenuentriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
