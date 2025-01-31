from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdForecastCopyIdEndpoint import (
    SalesOpportunitiesIdForecastCopyIdEndpoint,
)


class SalesOpportunitiesIdForecastCopyEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "copy", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> SalesOpportunitiesIdForecastCopyIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesIdForecastCopyIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOpportunitiesIdForecastCopyIdEndpoint: The initialized SalesOpportunitiesIdForecastCopyIdEndpoint object.
        """
        child = SalesOpportunitiesIdForecastCopyIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child
