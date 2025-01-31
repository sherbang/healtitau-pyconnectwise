from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdWorkroleexemptionsCountEndpoint import (
    FinanceTaxcodesIdWorkroleexemptionsCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdWorkroleexemptionsIdEndpoint import (
    FinanceTaxcodesIdWorkroleexemptionsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import WorkRoleExemption
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class FinanceTaxcodesIdWorkroleexemptionsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[WorkRoleExemption], ConnectWiseManageRequestParams],
    IPostable[WorkRoleExemption, ConnectWiseManageRequestParams],
    IPaginateable[WorkRoleExemption, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "workRoleExemptions", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[WorkRoleExemption])
        IPostable.__init__(self, WorkRoleExemption)
        IPaginateable.__init__(self, WorkRoleExemption)

        self.count = self._register_child_endpoint(
            FinanceTaxcodesIdWorkroleexemptionsCountEndpoint(
                client, parent_endpoint=self
            )
        )

    def id(
        self, id: int  # noqa: A002
    ) -> FinanceTaxcodesIdWorkroleexemptionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxcodesIdWorkroleexemptionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxcodesIdWorkroleexemptionsIdEndpoint: The initialized FinanceTaxcodesIdWorkroleexemptionsIdEndpoint object.
        """
        child = FinanceTaxcodesIdWorkroleexemptionsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[WorkRoleExemption]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/workRoleExemptions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkRoleExemption]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            WorkRoleExemption,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[WorkRoleExemption]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/workRoleExemptions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkRoleExemption]: The parsed response data.
        """
        return self._parse_many(
            WorkRoleExemption,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> WorkRoleExemption:
        """
        Performs a POST request against the /finance/taxCodes/{id}/workRoleExemptions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkRoleExemption: The parsed response data.
        """
        return self._parse_one(
            WorkRoleExemption,
            super()._make_request("POST", data=data, params=params).json(),
        )
