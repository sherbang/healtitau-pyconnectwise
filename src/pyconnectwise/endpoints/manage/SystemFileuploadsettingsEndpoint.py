from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemFileuploadsettingsCountEndpoint import (
    SystemFileuploadsettingsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemFileuploadsettingsIdEndpoint import (
    SystemFileuploadsettingsIdEndpoint,
)


class SystemFileuploadsettingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "fileuploadsettings", parent_endpoint=parent_endpoint
        )

        self.count = self._register_child_endpoint(
            SystemFileuploadsettingsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemFileuploadsettingsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SystemFileuploadsettingsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemFileuploadsettingsIdEndpoint: The initialized SystemFileuploadsettingsIdEndpoint object.
        """
        child = SystemFileuploadsettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
