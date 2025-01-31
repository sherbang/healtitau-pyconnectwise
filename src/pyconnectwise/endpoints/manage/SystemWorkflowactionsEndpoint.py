from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowactionsIdEndpoint import (
    SystemWorkflowactionsIdEndpoint,
)


class SystemWorkflowactionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "workflowActions", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> SystemWorkflowactionsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowactionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemWorkflowactionsIdEndpoint: The initialized SystemWorkflowactionsIdEndpoint object.
        """
        child = SystemWorkflowactionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
