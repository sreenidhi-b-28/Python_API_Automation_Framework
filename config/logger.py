import logging
import os


def setup_logger():
    folder_path = '../reports'
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    logger = logging.getLogger("API Python tests")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='../reports/API_Test.log')
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


logger = setup_logger()
