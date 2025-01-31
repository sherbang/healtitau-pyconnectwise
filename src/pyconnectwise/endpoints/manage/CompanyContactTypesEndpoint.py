from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactTypesIdEndpoint import (
    CompanyContactTypesIdEndpoint,
)


class CompanyContactTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "types", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> CompanyContactTypesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactTypesIdEndpoint: The initialized CompanyContactTypesIdEndpoint object.
        """
        child = CompanyContactTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
