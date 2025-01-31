from pyconnectwise.endpoints.automate.ComputersIdSoftwareIdUninstallEndpoint import (
    ComputersIdSoftwareIdUninstallEndpoint,
)
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class ComputersIdSoftwareIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )

        self.uninstall = self._register_child_endpoint(
            ComputersIdSoftwareIdUninstallEndpoint(client, parent_endpoint=self)
        )
