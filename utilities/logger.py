import logging

def define_logger(module, severity_level="DEBUG"):
    """
    severity_level - options are:
        NOTSET=0.
        DEBUG=10.
        INFO=20.
        WARN=30.
        ERROR=40.
        CRITICAL=50.
    """
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logger = logging.getLogger(module)
    logger.setLevel(severity_level)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(log_format)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger