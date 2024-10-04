import logging

def setup_logger(name, level=logging.DEBUG):

    # Create a custom logger
    logger = logging.getLogger(name)

    # Configure the custom logger
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(f"{name}.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger