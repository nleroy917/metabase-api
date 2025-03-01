from metabase import Metabase

def test_create_client():
    metabase = Metabase(host_url="http://localhost:3000", api_key="...")
    assert metabase.host_url == "http://localhost:3000"
    assert metabase.api_key == "..."