import pytest


@pytest.fixture(scope="class", autouse=True)
def url_setup(request):
    base_url = "https://reqres.in/api"
    request.cls.base_url = base_url
