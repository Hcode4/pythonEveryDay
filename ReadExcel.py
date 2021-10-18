# -*- coding: utf-8 -*-

import OpFactory

if __name__ == '__main__':
    # 读取Excel
    filePath = input("输入文件路径, 请将\\ 改为 / 如 C:/Users/16146/Desktop/test.xls\n")
    OpFactory.op_factory(filePath)

