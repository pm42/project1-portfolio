"""this tests the web page"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    # Arrange Data for AAA testing
    path = "/"

    # Act for AAA testing
    response = client.get(path)

    # Assertion for AAA testing
    assert response.status_code == 200
    assert b'<a class="nav-link active" href="/">Home </a>' in response.data
    assert b'<a class="nav-link " href="/git">Git </a>' in response.data
    assert b'<a class="nav-link " href="/docker">Docker </a>' in response.data
    assert b'<a class="nav-link " href="/flask">Python-Flask </a>' in response.data
    assert b'<a class="nav-link " href="/cicd">CI-CD </a>' in response.data
    assert b'<a class="nav-link " href="/glossary">Glossary </a>' in response.data
    assert b'<a class="nav-link " href="/aaa">AAA </a>' in response.data
    assert b'<a class="nav-link " href="/oop">OOP </a>' in response.data
    assert b'<a class="nav-link " href="/solid">SOLID </a>' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"<title>Portfolio - Home Page </title>" in response.data
    assert b'<li>Associate of the Quarter - Cognizant Technology Solutions</li>' in response.data
    assert b'<h5 class="card-title">Interests - Out Of Office</h5>' in response.data


def test_request_git(client):
    """This makes the git page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"<title>Portfolio - Git Page </title>" in response.data
    assert b'<p class="card-text">Git is a popular version control system.' in response.data
    assert b'<h6 class="card-title">Command: git commit -m ' \
           b'[descriptive message]</h6>' in response.data


def test_request_docker(client):
    """This makes the docker page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"<title>Portfolio - Docker Page </title>" in response.data
    assert b'<p class="card-text">Docker is an open platform for developing, shipping,' \
           b' and running applications.' in response.data
    assert b'<li>docker container create <p>Create a new container</p></li>' in response.data


def test_request_flask(client):
    """This makes the python flask page"""
    response = client.get("/flask")
    assert response.status_code == 200
    assert b"<title>Portfolio - Flask Page </title>" in response.data
    assert b'It does have many cool features like url routing, template' in response.data
    assert b'<h5 class="card-header">Testing Flask Applications Using Pytest</h5>' in response.data


def test_request_cicd(client):
    """This makes the continuous integration and deployment page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"<title>Portfolio - CICD Page </title>" in response.data
    assert b'<h2 class="card-header">Continuous Integration and Deployment</h2>' in response.data
    assert b'<div class="card-header text-dark">Code Review Process</div>' in response.data


def test_request_glossary(client):
    """This makes the Glossary page"""
    response = client.get("/glossary")
    assert response.status_code == 200
    assert b"<title>Portfolio - Glossary Page </title>" in response.data
    assert b"<h5 class=\"card-title\">Class</h5>" in response.data


def test_request_aaa(client):
    """This makes the AAA page"""
    response = client.get("/aaa")
    assert response.status_code == 200
    assert b"<title>Portfolio - AAA Page </title>" in response.data
    assert b" <h5 class=\"card-title\">AAA - A Pattern for writing good tests</h5>" in response.data


def test_request_oop(client):
    """This makes the OOP page"""
    response = client.get("/oop")
    assert response.status_code == 200
    assert b"<title>Portfolio - OOP Page </title>" in response.data
    assert b" <h5 class=\"card-title\">Encapsulation in Calculator</h5>" in response.data


def test_request_solid(client):
    """This makes the SOLID page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b"<title>Portfolio - SOLID Page </title>" in response.data
    assert b"<h5 class=\"card-title\">Dependency Inversion Principle " \
           b"in Calculator</h5>" in response.data
