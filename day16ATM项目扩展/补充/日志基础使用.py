"""
python里的日志模块: logging
python的logging模块是标准库中用于日志记录的核心工具，支持灵活的日志级别控制、多输出目标(文件、控制台等)、
自定义格式及扩展功能。
    Logger（日志记录器）     ← 你在代码中调用的接口
    Handler（日志处理器）    ← 决定日志输出到哪里（终端、文件等）
    Formatter（格式器）      ← 决定日志内容怎么显示


1、日志级别
    按严重程度，从低到高分为5个级别，可以通过设置级别过滤日志输出
        DEBUG: 调试信息,仅开发阶段使用
        INFO: 普通运行信息
        WARNING: 警告信息（不影响程序运行，但需要关注的时候）
        ERROR: 错误信息
        CRITICAL: 严重错误

2 日志格式化
    %(asctime)s:  日志记录时间(默认格式 YYYY-MM-DD HH:MM:SS,sss)
    %(levelname)s: 日志级别(DEBUG\INFO)
    %(name)s: 日志器的名称(通常使用模块名，便于定位来源)
    %(message)s: 日志消息内容
    %(module)s: 模块名
    %(lineno)d: 行号(快速定位代码位置)
    %(process)d / %(thread)d: 进程、线程ID

2. 日志处理器（Handlers）
    控制日志的输出目标和方式，支持多目标输出（如控制台、文件、网络等）：
        StreamHandler：默认输出到控制台（stdout/stderr）。
        FileHandler：输出到指定文件（支持w/a模式）。
        RotatingFileHandler：按文件大小轮转日志（如超过5MB自动创建新文件）。
        TimedRotatingFileHandler：按时间轮转日志（如每天/每周创建新文件）。
        SMTPHandler：通过邮件发送日志（适用于严重错误告警）。
"""
import logging

# 基础配置
logging.basicConfig(
    level=logging.INFO,  # 级别
    format="%(asctime)s - %(name)s - %(levelname)s -%(message)s",  # 格式
    handlers=[
        logging.StreamHandler(),  # 输出到控制台
        logging.FileHandler("my_app.log", encoding="utf-8"),  # 输出到文件
    ],
)

# 默认只显示warning及以上的信息
# 不显示
logging.debug("这是一个调试信息!")
logging.info("这是一个普通信息!")

# 显示了
logging.warning("这是一个警告信息!")
logging.error("这是一个错误信息!")
logging.critical("这是一个严重错误信息!")

