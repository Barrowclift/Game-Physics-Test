#!/usr/bin/python3

__author__ = "Marc Barrowclift"
__copyright__ = "Copyright 2014, Marc Barrowclift"

__version__ = "0.1"
__email__ = "meb77@icloud.com"
__license__ = "GPL"

import sys

sys.path.append("./helpers/")
sys.path.append("./managers/")
sys.path.append("./elements/")


import windowManager

windowManager.init()
windowManager.run()