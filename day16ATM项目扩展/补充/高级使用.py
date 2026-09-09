import logging

# 创建logger对象
logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)

# 创建文件处理器
file_handler = logging.FileHandler('app.log', encoding="utf-8")
# 单独设置文件处理器的级别 INFO
file_handler.setLevel(logging.INFO)

# 创建控制台处理器
console_handler = logging.StreamHandler()
# 单独设置控制台处理器的级别 DEBUG
console_handler.setLevel(logging.DEBUG)

# 创建格式器
# -8s 表示左对齐，宽度8个字符
formatter = logging.Formatter('[%(asctime)s %(name)s] %(levelname)-8s | %(module)s:%(lineno)d | %(message)s')
# 设置格式化器
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 添加处理器到logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.debug("DEBUG调试信息")
logger.info("INFO普通信息")
logger.warning("WARNING: 警告信息（不影响程序运行，但需要关注的时候）")
logger.error("ERROR: 错误信息")
logger.critical("CRITICAL: 严重错误")
