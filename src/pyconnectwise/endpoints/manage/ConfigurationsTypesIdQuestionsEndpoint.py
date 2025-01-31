from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ConfigurationsTypesIdQuestionsIdEndpoint import (
    ConfigurationsTypesIdQuestionsIdEndpoint,
)
from pyconnectwise.endpoints.manage.ConfigurationsTypesIdQuestionsInfoEndpoint import (
    ConfigurationsTypesIdQuestionsInfoEndpoint,
)


class ConfigurationsTypesIdQuestionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "questions", parent_endpoint=parent_endpoint
        )

        self.info = self._register_child_endpoint(
            ConfigurationsTypesIdQuestionsInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ConfigurationsTypesIdQuestionsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ConfigurationsTypesIdQuestionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ConfigurationsTypesIdQuestionsIdEndpoint: The initialized ConfigurationsTypesIdQuestionsIdEndpoint object.
        """
        child = ConfigurationsTypesIdQuestionsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child
