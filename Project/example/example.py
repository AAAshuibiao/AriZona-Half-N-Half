import os
import sys
sys.path.append("../auto_grader/")
from auto_grader import auto_grader
ag = auto_grader()
# 读入图片
while True:
    lst = []
    for i in range(4):
        lst.append(int(input()))
    ag.link(*lst)
os.system('pause')
