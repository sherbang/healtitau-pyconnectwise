from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsTypesIdInfoEndpoint import (
    MarketingCampaignsTypesIdInfoEndpoint,
)
from pyconnectwise.endpoints.manage.MarketingCampaignsTypesIdSubtypesEndpoint import (
    MarketingCampaignsTypesIdSubtypesEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import CampaignType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class MarketingCampaignsTypesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[CampaignType, ConnectWiseManageRequestParams],
    IPuttable[CampaignType, ConnectWiseManageRequestParams],
    IPatchable[CampaignType, ConnectWiseManageRequestParams],
    IPaginateable[CampaignType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, CampaignType)
        IPuttable.__init__(self, CampaignType)
        IPatchable.__init__(self, CampaignType)
        IPaginateable.__init__(self, CampaignType)

        self.sub_types = self._register_child_endpoint(
            MarketingCampaignsTypesIdSubtypesEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            MarketingCampaignsTypesIdInfoEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[CampaignType]:
        """
        Performs a GET request against the /marketing/campaigns/types/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CampaignType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            CampaignType,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> CampaignType:
        """
        Performs a GET request against the /marketing/campaigns/types/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CampaignType: The parsed response data.
        """
        return self._parse_one(
            CampaignType, super()._make_request("GET", data=data, params=params).json()
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /marketing/campaigns/types/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> CampaignType:
        """
        Performs a PUT request against the /marketing/campaigns/types/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CampaignType: The parsed response data.
        """
        return self._parse_one(
            CampaignType, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> CampaignType:
        """
        Performs a PATCH request against the /marketing/campaigns/types/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CampaignType: The parsed response data.
        """
        return self._parse_one(
            CampaignType,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
