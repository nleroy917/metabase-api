from requests import Session

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
        