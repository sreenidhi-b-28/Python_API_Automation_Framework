import pytest
from endpoints.login import ApiRegister
from config.logger import logger

@pytest.mark.usefixtures("url_setup")
class TestRegister:

    def test_register(self):
        """Test method to check the registration endpoint"""
        logger.info("Check registration endpoints")
        post_api = ApiRegister(base_url=self.base_url)
        status_code, response = post_api.register("eve.holt@reqres.in", "pistol")
        logger.info(f"Status code: {status_code}")
        assert status_code == 200
        assert response['id'] == 4
        assert response['token'] == "QpwL5tke4Pnpja7X4"

    def test_negative_register(self):
        """Test method to check without the password"""
        logger.info("Check registration endpoints without providing password")
        post_api = ApiRegister(base_url=self.base_url)
        status_code, response = post_api.register("eve.holt@reqres.in")
        assert status_code == 400
        logger.info(f"Status code: {status_code}")
        logger.info(f"Error message: {response['error']}")
        assert response['error'] == "Missing password"
