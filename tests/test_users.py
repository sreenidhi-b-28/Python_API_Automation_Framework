import pytest
import os
import pandas as pd
from endpoints.users import ApiUsers
from data_loaders.user_data import users_data
from config.logger import logger


@pytest.mark.usefixtures("url_setup")
class TestUsers:

    def test_get_users(self):
        """Test method to check the get user endpoint"""
        get_api = ApiUsers(base_url=self.base_url)
        status_code, response = get_api.list_users()
        assert status_code == 200
        assert response

    def test_get_resource(self):
        """Test method to check the get resource endpoint"""
        logger.info("Get resource details")
        get_api = ApiUsers(base_url=self.base_url)
        status_code, response = get_api.list_users()
        logger.info(f"Status code: {status_code}")
        assert status_code == 200
        assert response

    def test_create_user(self):
        """Test method to create the users"""
        logger.info("Post method to create user records")
        post_api = ApiUsers(base_url=self.base_url)
        """Empty list to store the values"""
        excel_data = []
        for user_data in users_data:
            status_code, response = post_api.create_users(user_data[0], user_data[1])
            name = response.get('name')
            job = response.get('job')
            id = response.get('id')
            created_at = response.get('createdAt')
            logger.info(f"User {name} created with status code {status_code}")
            excel_data.append({"Name": name, "Job": job, "ID": id, "CreatedAt": created_at, "Status Code": status_code})

        """Create the excel sheet and save the response of the users data that has been created"""
        df = pd.DataFrame(excel_data)
        folder_path = '../output_data'
        file_path = '../output_data/users_data.xlsx'
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name="User Data")

    def test_update_user(self):
        """Test method to check put update"""
        logger.info("To update the user")
        put_api = ApiUsers(base_url=self.base_url)
        status_code, response = put_api.update_user("Tom", "HR")
        logger.info(f"Status code: {status_code}")
        logger.info(f"Response: {response}")
        assert status_code == 201
        assert response['name'] == "Tom"
        assert response["job"] == "HR"

    def test_partial_update_user(self):
        """Test method to check the partial update endpoint"""
        logger.info("To update the resource partially")
        put_api = ApiUsers(base_url=self.base_url)
        status_code, response = put_api.partial_update_user("Accounts")
        logger.info(f"Status code: {status_code} and Job: {response['job']}")
        assert status_code == 201
        assert response["job"] == "Accounts"
