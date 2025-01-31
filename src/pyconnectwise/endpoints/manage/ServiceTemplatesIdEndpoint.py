from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceTemplatesIdGenerateEndpoint import (
    ServiceTemplatesIdGenerateEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceTemplatesIdInfoEndpoint import (
    ServiceTemplatesIdInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import ServiceTemplate
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ServiceTemplatesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[ServiceTemplate, ConnectWiseManageRequestParams],
    IPaginateable[ServiceTemplate, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, ServiceTemplate)
        IPaginateable.__init__(self, ServiceTemplate)

        self.generate = self._register_child_endpoint(
            ServiceTemplatesIdGenerateEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            ServiceTemplatesIdInfoEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ServiceTemplate]:
        """
        Performs a GET request against the /service/templates/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceTemplate]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ServiceTemplate,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ServiceTemplate:
        """
        Performs a GET request against the /service/templates/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceTemplate: The parsed response data.
        """
        return self._parse_one(
            ServiceTemplate,
            super()._make_request("GET", data=data, params=params).json(),
        )
