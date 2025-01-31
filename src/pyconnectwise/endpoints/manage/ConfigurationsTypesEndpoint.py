from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ConfigurationsTypesIdEndpoint import (
    ConfigurationsTypesIdEndpoint,
)
from pyconnectwise.endpoints.manage.ConfigurationsTypesInfoEndpoint import (
    ConfigurationsTypesInfoEndpoint,
)


class ConfigurationsTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "types", parent_endpoint=parent_endpoint
        )

        self.info = self._register_child_endpoint(
            ConfigurationsTypesInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ConfigurationsTypesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ConfigurationsTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ConfigurationsTypesIdEndpoint: The initialized ConfigurationsTypesIdEndpoint object.
        """
        child = ConfigurationsTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
