from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import BoardTypeSubTypeItemAssociation
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ServiceBoardsIdTypesubtypeitemassociationsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[BoardTypeSubTypeItemAssociation, ConnectWiseManageRequestParams],
    IPaginateable[BoardTypeSubTypeItemAssociation, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, BoardTypeSubTypeItemAssociation)
        IPaginateable.__init__(self, BoardTypeSubTypeItemAssociation)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[BoardTypeSubTypeItemAssociation]:
        """
        Performs a GET request against the /service/boards/{id}/typeSubTypeItemAssociations/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardTypeSubTypeItemAssociation]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            BoardTypeSubTypeItemAssociation,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> BoardTypeSubTypeItemAssociation:
        """
        Performs a GET request against the /service/boards/{id}/typeSubTypeItemAssociations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardTypeSubTypeItemAssociation: The parsed response data.
        """
        return self._parse_one(
            BoardTypeSubTypeItemAssociation,
            super()._make_request("GET", data=data, params=params).json(),
        )
