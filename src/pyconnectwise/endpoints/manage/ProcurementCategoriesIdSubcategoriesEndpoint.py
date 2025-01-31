from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementCategoriesIdSubcategoriesCountEndpoint import (
    ProcurementCategoriesIdSubcategoriesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementCategoriesIdSubcategoriesIdEndpoint import (
    ProcurementCategoriesIdSubcategoriesIdEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementCategoriesIdSubcategoriesInfoEndpoint import (
    ProcurementCategoriesIdSubcategoriesInfoEndpoint,
)


class ProcurementCategoriesIdSubcategoriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "subcategories", parent_endpoint=parent_endpoint
        )

        self.count = self._register_child_endpoint(
            ProcurementCategoriesIdSubcategoriesCountEndpoint(
                client, parent_endpoint=self
            )
        )
        self.info = self._register_child_endpoint(
            ProcurementCategoriesIdSubcategoriesInfoEndpoint(
                client, parent_endpoint=self
            )
        )

    def id(
        self, id: int  # noqa: A002
    ) -> ProcurementCategoriesIdSubcategoriesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementCategoriesIdSubcategoriesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementCategoriesIdSubcategoriesIdEndpoint: The initialized ProcurementCategoriesIdSubcategoriesIdEndpoint object.
        """
        child = ProcurementCategoriesIdSubcategoriesIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child
