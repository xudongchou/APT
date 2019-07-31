"""
@project:code
@author:lenovo
@file:Logs.py
@ide:PyCharm
@time:2019/6/10 14:56
@month:六月

"""

"""
@crt_handler: CUI handler
@f_handler:  File handler
@logger: log interface variable
use exp:
logger=logs()
logger.info("hello world!")
"""
import logging
import logging.handlers
import os,sys,time
def logs():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    crt_handler=logging.StreamHandler(sys.stderr)
    crt_handler.setLevel(logging.INFO)
    crt_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(message)s"))
    log_time = time.strftime("%Y-%m-%d_%H:%M:%S")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(base_dir)
    log_path = base_dir+'\\Logs\\'
    log_name = log_path + log_time + 'error.log'
    print(log_name)
    f_handler = logging.FileHandler(log_name)
    f_handler.setLevel(logging.DEBUG)
    f_handler.setFormatter(logging.Formatter("%(asctime)s -%(name)s -%(message)s"))
    logger.addHandler(crt_handler)
    logger.addHandler(f_handler)
    return logger


logger = logs()
