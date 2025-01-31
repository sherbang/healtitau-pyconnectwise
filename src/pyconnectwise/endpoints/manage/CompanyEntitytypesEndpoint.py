from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyEntitytypesIdEndpoint import (
    CompanyEntitytypesIdEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyEntitytypesInfoEndpoint import (
    CompanyEntitytypesInfoEndpoint,
)


class CompanyEntitytypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "entitytypes", parent_endpoint=parent_endpoint
        )

        self.info = self._register_child_endpoint(
            CompanyEntitytypesInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyEntitytypesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized CompanyEntitytypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyEntitytypesIdEndpoint: The initialized CompanyEntitytypesIdEndpoint object.
        """
        child = CompanyEntitytypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
