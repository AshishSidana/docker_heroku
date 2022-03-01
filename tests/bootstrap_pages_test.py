"""This test the bootstrappage"""


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/home")
    assert response.status_code == 200
    assert b"Layout" in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"Layout" in response.data