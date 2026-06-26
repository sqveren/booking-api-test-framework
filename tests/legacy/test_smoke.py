from client.api_client import APIClient


def test_get_posts():
    client = APIClient("https://jsonplaceholder.typicode.com")
    response = client.get("/posts")

    assert response.status_code == 200

    posts = response.json()

    assert isinstance(posts,list)
    assert len(posts) > 0 , "Data is empty"
    assert "id" in posts[0]
    assert "title" in posts[0]

