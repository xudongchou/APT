import yaml
import configparser
import os

"""
常用的基本方法
"""
# def load_config():
#     config_file = os.path.join(os.path.join(os.getcwd(), "config", "run_config.ini"))
#     cf = configparser.ConfigParser()
#     cf.read(config_file)
#     ip = dict(cf.items("Run Test"))["ip"]
#     user_device_suffix = dict(cf.items("Run Test"))['user_device_suffix']
#     port = dict(cf.items("Run Test"))['port']
#     prefix = dict(cf.items("Run Test"))['prefix']
#     device_suffix = dict(cf.items("Run Test"))['device_suffix']
#     executor = dict(cf.items("Run Test"))['executor']
#     return {
#         'ip': ip,
#         'user_device_suffix': user_device_suffix,
#         'device_suffix': device_suffix,
#         'port': port,
#         'prefix': prefix,
#         'executor': executor
#     }


def load_caps(serial):
    cap_file = open(os.path.join(os.getcwd(), "config", "caps.yaml"), "rb")
    result = yaml.load(cap_file)
    cap_file.close()
    for device in result.values():
        if device["deviceName"] == serial:
            desired_caps = device
            return desired_caps
            break
def load_caps():
    cap_file = open(os.path.join(os.getcwd(), "config", "caps.yaml"), "rb")
    result = yaml.load(cap_file)
    cap_file.close()
    for device in result.values():
        if device["deviceName"]:
            desired_caps = device
            return desired_caps

