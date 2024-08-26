import pandas as pd


file_name = '../data/users.xlsx'


def user_data():
    data_of_users = pd.read_excel(file_name)
    return data_of_users.values.tolist()


users_data = user_data()
