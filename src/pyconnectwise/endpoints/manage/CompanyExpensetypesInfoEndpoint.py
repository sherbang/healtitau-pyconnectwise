from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyExpensetypesInfoCountEndpoint import (
    CompanyExpensetypesInfoCountEndpoint,
)


class CompanyExpensetypesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "info", parent_endpoint=parent_endpoint
        )

        self.count = self._register_child_endpoint(
            CompanyExpensetypesInfoCountEndpoint(client, parent_endpoint=self)
        )
