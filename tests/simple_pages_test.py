"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/">Home </a>' in response.data
    assert b'<a class="nav-link" href="/git">Git </a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker </a>' in response.data
    assert b'<a class="nav-link" href="/flask">Python-Flask </a>' in response.data
    assert b'<a class="nav-link" href="/cicd">CI-CD </a>' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<h5 class="card-title">About Me</h5>' in response.data
    assert b'<li>Associate of the Quarter - Cognizant Technology Solutions</li>' in response.data
    assert b'<h5 class="card-title">Interests - Out Of Office</h5>' in response.data


