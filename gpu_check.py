#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())