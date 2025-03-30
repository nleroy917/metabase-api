from requests import Session, Response

from metabase.const import DEFAULT_METABASE_HOST
from metabase.exceptions import MissingParameterException

from .models import UsageStats

class Metabase:
    def __init__(self, host_url: str = None, api_key: str = None, kwargs: dict = dict()):
        """
        Initialize the Metabase API client.


        :param host_url: The URL of the Metabase instance.
        :param api_key: The API key
        :param kwargs: Additional options

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
            f"{self.host_url}{path}"
        )
    
    def _post(self, path: str, data: dict) -> Response:
        """
        Send a POST request to the Metabase API.

        :param path: The path to send the request to.
        :param data: The data to send.
        """
        return self.session.post(
            f"{self.host_url}{path}",
            json=data
        )
    
    def _delete(self, path: str) -> Response:
        """
        Send a DELETE request to the Metabase API.

        :param path: The path to send the request to.
        """
        return self.session.delete(
            f"{self.host_url}{path}"
        )
    
    def _put(self, path: str, data: dict) -> Response:
        """
        Send a PUT request to the Metabase API.

        :param path: The path to send the request to.
        :param data: The data to send.
        """
        return self.session.put(
            f"{self.host_url}{path}",
            json=data
        )
    
    def _patch(self, path: str, data: dict) -> Response:
        """
        Send a PATCH request to the Metabase API.

        :param path: The path to send the request to.
        :param data: The data to send.
        """
        return self.session.patch(
            f"{self.host_url}{path}",
            json=data
        )
    
    def get_user(self, user_id: int) -> Response:
        """
        Get a user by ID.

        :param user_id: The ID of the user.
        """
        return self._get(f"/api/user/{user_id}")
    
    def create_new_user(self, email: str = None, first_name: str = None, last_name: str = None, login_attributes: dict = None, user_group_memberships: list[dict] = None) -> Response:
        """
        Create a new user in Metabase.

        :param email: The email of the new user.
        :param first_name: The first name of the new user.
        :param last_name: The last name of the new user.
        :param login_attributes: Additional login attributes for the new user.
        :param user_group_memberships: List of user group memberships.
        """
        if email is None:
            raise MissingParameterException("email")
        data = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "login_attributes": login_attributes,
            "user_group_memberships": user_group_memberships
        }
        return self._post("/api/user", data)
    
    def sync_database_schema(self, database_id: int) -> Response:
        """
        Trigger a manual update of the schema metadata for this database.

        :param database_id: The ID of the database.
        """
        return self._post(f"/api/database/{database_id}/sync_schema", {})
    
    def stats(self) -> Response:
        """
        Anonymous usage stats. Endpoint for testing, and eventually exposing this to instance admins to let them see what is being phoned home. 
        """
        response = self._get("/api/util/stats")
        response.raise_for_status()
        return UsageStats(**response.json())
    
    def __repr__(self):
        """
        Return a string representation of the Metabase API client.

        :return: A string representation of the Metabase API client.
        """
        return f"Metabase(host_url={self.host_url}, api_key={self.api_key[0:5]}*****)"
    
    def __str__(self):
        """
        Return a string representation of the Metabase API client.

        :return: A string representation of the Metabase API client.
        """
        return f"Metabase API Client (host_url={self.host_url})"