import logging


def setup_logger():
    logger = logging.getLogger("API Python tests")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='../output_data/API_Test.log')
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


logger = setup_logger()
