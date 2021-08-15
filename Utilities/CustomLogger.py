import logging


class LogGen:
    @staticmethod
    def loggen():
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%m/%d/%Y %I:%s  %p")
        handler = logging.FileHandler(filename='.//Logs//automation.log')
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        return logger
