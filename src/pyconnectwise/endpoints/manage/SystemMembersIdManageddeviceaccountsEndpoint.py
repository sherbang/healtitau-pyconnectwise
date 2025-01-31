from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdManageddeviceaccountsBulkEndpoint import (
    SystemMembersIdManageddeviceaccountsBulkEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import ManagedDeviceAccount
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemMembersIdManageddeviceaccountsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ManagedDeviceAccount], ConnectWiseManageRequestParams],
    IPaginateable[ManagedDeviceAccount, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "managedDeviceAccounts", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ManagedDeviceAccount])
        IPaginateable.__init__(self, ManagedDeviceAccount)

        self.bulk = self._register_child_endpoint(
            SystemMembersIdManageddeviceaccountsBulkEndpoint(
                client, parent_endpoint=self
            )
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ManagedDeviceAccount]:
        """
        Performs a GET request against the /system/members/{id}/managedDeviceAccounts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagedDeviceAccount]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ManagedDeviceAccount,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ManagedDeviceAccount]:
        """
        Performs a GET request against the /system/members/{id}/managedDeviceAccounts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManagedDeviceAccount]: The parsed response data.
        """
        return self._parse_many(
            ManagedDeviceAccount,
            super()._make_request("GET", data=data, params=params).json(),
        )
