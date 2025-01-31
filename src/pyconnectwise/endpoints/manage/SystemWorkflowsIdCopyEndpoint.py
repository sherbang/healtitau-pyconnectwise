from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPostable,
)
from pyconnectwise.models.manage import Workflow
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemWorkflowsIdCopyEndpoint(
    ConnectWiseEndpoint, IPostable[Workflow, ConnectWiseManageRequestParams]
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "copy", parent_endpoint=parent_endpoint
        )
        IPostable.__init__(self, Workflow)

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Workflow:
        """
        Performs a POST request against the /system/workflows/{id}/copy endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Workflow: The parsed response data.
        """
        return self._parse_one(
            Workflow, super()._make_request("POST", data=data, params=params).json()
        )
