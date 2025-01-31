from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemM365contactsyncIdInfoEndpoint import (
    SystemM365contactsyncIdInfoEndpoint,
)
from pyconnectwise.endpoints.manage.SystemM365contactsyncIdTestEndpoint import (
    SystemM365contactsyncIdTestEndpoint,
)
from pyconnectwise.endpoints.manage.SystemM365contactsyncIdViewauthEndpoint import (
    SystemM365contactsyncIdViewauthEndpoint,
)


class SystemM365contactsyncIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )

        self.test = self._register_child_endpoint(
            SystemM365contactsyncIdTestEndpoint(client, parent_endpoint=self)
        )
        self.viewauth = self._register_child_endpoint(
            SystemM365contactsyncIdViewauthEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            SystemM365contactsyncIdInfoEndpoint(client, parent_endpoint=self)
        )
