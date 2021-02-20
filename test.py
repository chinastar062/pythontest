#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import os
import random

# 某科学的一方变量
local = time.localtime(time.time())
a = int(random.randint(10, 200))
b = os.getcwd()
# 写入文件
for i in range(a):
    f = open(b+'/1.txt', 'a')
    f.write('\n'+str(local))
    f.close()
