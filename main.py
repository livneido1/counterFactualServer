# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
import datetime

from BussinessLayer.Logger import Logger
import BussinessLayer.SystemConfig as SystemConfig
import os
from pathlib import Path

if __name__ == '__main__':
    config = SystemConfig.SystemConfig()
    logger = Logger(config)
    logger.debug("check here")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
