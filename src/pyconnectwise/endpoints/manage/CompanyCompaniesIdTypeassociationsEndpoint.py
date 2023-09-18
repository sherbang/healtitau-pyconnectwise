from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdTypeassociationsCountEndpoint import \
    CompanyCompaniesIdTypeassociationsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdTypeassociationsIdEndpoint import \
    CompanyCompaniesIdTypeassociationsIdEndpoint
from pyconnectwise.models.manage import CompanyCompanyTypeAssociationCompanyTypeAssociation
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyCompaniesIdTypeassociationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "typeAssociations", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            CompanyCompaniesIdTypeassociationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyCompaniesIdTypeassociationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesIdTypeassociationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesIdTypeassociationsIdEndpoint: The initialized CompanyCompaniesIdTypeassociationsIdEndpoint object.
        """
        child = CompanyCompaniesIdTypeassociationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[CompanyCompanyTypeAssociationCompanyTypeAssociation]:
        """
        Performs a GET request against the /company/companies/{id}/typeAssociations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyCompanyTypeAssociationCompanyTypeAssociation]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            CompanyCompanyTypeAssociationCompanyTypeAssociation,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> list[CompanyCompanyTypeAssociationCompanyTypeAssociation]:
        """
        Performs a GET request against the /company/companies/{id}/typeAssociations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyCompanyTypeAssociationCompanyTypeAssociation]: The parsed response data.
        """
        return self._parse_many(
            CompanyCompanyTypeAssociationCompanyTypeAssociation,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> CompanyCompanyTypeAssociationCompanyTypeAssociation:
        """
        Performs a POST request against the /company/companies/{id}/typeAssociations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyCompanyTypeAssociationCompanyTypeAssociation: The parsed response data.
        """
        return self._parse_one(
            CompanyCompanyTypeAssociationCompanyTypeAssociation,
            super()._make_request("POST", data=data, params=params).json(),
        )
