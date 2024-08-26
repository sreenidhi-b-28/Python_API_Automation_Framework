import pytest
from endpoints.login import ApiRegister


@pytest.mark.usefixtures("url_setup")
class TestRegister:

    def test_register(self):
        """Test method to check the get user endpoint"""
        post_api = ApiRegister(base_url=self.base_url)
        status_code, response = post_api.register("eve.holt@reqres.in", "pistol")
        assert status_code == 200
        assert response['id'] == 4
        assert response['token'] == "QpwL5tke4Pnpja7X4"

    def test_negative_register(self):
        post_api = ApiRegister(base_url=self.base_url)
        status_code, response = post_api.register("eve.holt@reqres.in")
        assert status_code == 400
        assert response['error'] == "Missing password"

