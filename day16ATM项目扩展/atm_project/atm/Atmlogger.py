import logging

# 日志路径
LOG_FILE = "atm.log"

# 配置
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="[%(asctime)s %(name)s] %(levelname)s %(module)s:%(lineno)d >>> %(message)s",
    filemode="a",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)


def log_action(logger, msg, level="INFO"):
    """
    记录用户操作
    :param logger:
    :param msg:
    :param level:
    :return:
    """
    if level.lower() == "debug":
        logger.debug(msg)
    elif level.lower() == "info":
        logger.info(msg)
    elif level.lower() == "warning":
        logger.warning(msg)
    elif level.lower() == "error":
        logger.error(msg)
    elif level.lower() == "critical":
        logger.critical(msg)
    else:
        logger.info(msg)
