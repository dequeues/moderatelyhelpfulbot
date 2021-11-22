import logging
import os


def init_logger(logger_name, filename=None):
    if not filename:
        filename = os.path.join(logger_name + ".log")
    ilogger = logging.getLogger(logger_name)
    ilogger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    # create formatter
    # formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # add formatter
    # logger.setFormatter(formatter)
    # sh.setFormatter(formatter)
    # add ch to logger
    if len(ilogger.handlers) == 0:
        # logger.addHandler(file_logger)
        ilogger.addHandler(stream_handler)
    return ilogger


logger = init_logger("mhbot_log")
