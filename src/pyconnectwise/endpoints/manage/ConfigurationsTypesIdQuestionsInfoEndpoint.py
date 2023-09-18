from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ConfigurationsTypesIdQuestionsInfoCountEndpoint import \
    ConfigurationsTypesIdQuestionsInfoCountEndpoint
from pyconnectwise.models.manage import ConfigurationTypeQuestionInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ConfigurationsTypesIdQuestionsInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ConfigurationsTypesIdQuestionsInfoCountEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ConfigurationTypeQuestionInfo]:
        """
        Performs a GET request against the /configurations/types/{id}/questions/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ConfigurationTypeQuestionInfo]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ConfigurationTypeQuestionInfo, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ConfigurationTypeQuestionInfo]:
        """
        Performs a GET request against the /configurations/types/{id}/questions/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ConfigurationTypeQuestionInfo]: The parsed response data.
        """
        return self._parse_many(
            ConfigurationTypeQuestionInfo, super()._make_request("GET", data=data, params=params).json()
        )
