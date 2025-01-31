from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementSettingsCountEndpoint import (
    ProcurementSettingsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementSettingsIdEndpoint import (
    ProcurementSettingsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import ProcurementSetting
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ProcurementSettingsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ProcurementSetting], ConnectWiseManageRequestParams],
    IPaginateable[ProcurementSetting, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "settings", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ProcurementSetting])
        IPaginateable.__init__(self, ProcurementSetting)

        self.count = self._register_child_endpoint(
            ProcurementSettingsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementSettingsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ProcurementSettingsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementSettingsIdEndpoint: The initialized ProcurementSettingsIdEndpoint object.
        """
        child = ProcurementSettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ProcurementSetting]:
        """
        Performs a GET request against the /procurement/settings endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProcurementSetting]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ProcurementSetting,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ProcurementSetting]:
        """
        Performs a GET request against the /procurement/settings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProcurementSetting]: The parsed response data.
        """
        return self._parse_many(
            ProcurementSetting,
            super()._make_request("GET", data=data, params=params).json(),
        )
