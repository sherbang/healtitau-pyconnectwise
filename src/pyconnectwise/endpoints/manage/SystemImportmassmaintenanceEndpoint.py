from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemImportmassmaintenanceIdEndpoint import (
    SystemImportmassmaintenanceIdEndpoint,
)


class SystemImportmassmaintenanceEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "importMassMaintenance", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> SystemImportmassmaintenanceIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SystemImportmassmaintenanceIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemImportmassmaintenanceIdEndpoint: The initialized SystemImportmassmaintenanceIdEndpoint object.
        """
        child = SystemImportmassmaintenanceIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
