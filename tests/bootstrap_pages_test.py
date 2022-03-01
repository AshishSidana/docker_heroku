"""This test the bootstrappage"""


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/bootstrap")
    assert response.status_code == 200
    assert b"Layout" in response.data
