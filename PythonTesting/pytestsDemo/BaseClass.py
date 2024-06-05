import inspect
import logging

class BaseClass:
    def getLogger(self):
        LoggerName = inspect.stack()[1][3]
        logger = logging.getLogger(LoggerName)
        fileHandler = logging.FileHandler('logfile.log')
        Formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(Formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger