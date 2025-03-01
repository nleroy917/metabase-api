from requests import Session, Response

from .const import DEFAULT_METABASE_HOST

class Metabase:
    def __init__(self, host_url: str = None, api_key: str = None, kwargs: dict = None):
        """
        Initialize the Metabase API client.

        ```python
        from metabase import MetabaseAPI

        metabase = MetabaseAPI(host_url="http://localhost:3000", api_key="...")

        res = metabase.create_card(
            collection_id=1,
            name="My Card",
            dataset_query={
                "database": 1,
                "query": {
                    "source-table": 1
                }
            }
        )
        ```

        :param host_url: The URL of the Metabase instance.
        :param api_key: The API key
        :param kwargs: Additional options
        """
        self.host_url = host_url or DEFAULT_METABASE_HOST
        self.api_key = api_key
        self.session = Session(
            **kwargs
        )
        self.session.headers.update({
            "x-api-key": api_key
        })
    
    def _get(self, path: str) -> Response:
        """
        Send a GET request to the Metabase API.

        :param path: The path to send the request to.
        """
        return self.session.get(
            f"{self.host_url}/{path}"
        )
    
    def _post(self, path: str, data: dict) -> Response:
        """
        Send a POST request to the Metabase API.

        :param path: The path to send the request to.
        :param data: The data to send.
        """
        return self.session.post(
            f"{self.host_url}/{path}",
            json=data
        )
    
    def _delete(self, path: str) -> Response:
        """
        Send a DELETE request to the Metabase API.

        :param path: The path to send the request to.
        """
        return self.session.delete(
            f"{self.host_url}/{path}"
        )
    
    def _put(self, path: str, data: dict) -> Response:
        """
        Send a PUT request to the Metabase API.

        :param path: The path to send the request to.
        :param data: The data to send.
        """
        return self.session.put(
            f"{self.host_url}/{path}",
            json=data
        )
    
    def _patch(self, path: str, data: dict) -> Response:
        """
        Send a PATCH request to the Metabase API.

        :param path: The path to send the request to.
        :param data: The data to send.
        """
        return self.session.patch(
            f"{self.host_url}/{path}",
            json=data
        )