from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsUserdefinedfieldsActionsIdEndpoint import (
    SystemWorkflowsUserdefinedfieldsActionsIdEndpoint,
)


class SystemWorkflowsUserdefinedfieldsActionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "actions", parent_endpoint=parent_endpoint
        )

    def id(
        self, id: int  # noqa: A002
    ) -> SystemWorkflowsUserdefinedfieldsActionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowsUserdefinedfieldsActionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemWorkflowsUserdefinedfieldsActionsIdEndpoint: The initialized SystemWorkflowsUserdefinedfieldsActionsIdEndpoint object.
        """
        child = SystemWorkflowsUserdefinedfieldsActionsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child
