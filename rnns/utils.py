# -*- coding:utf-8 -*-
__author__ = 'EricDoug'
import csv

def f_write(rows, file, header=None):
    """
    写文件
    :param write_lists: 列表数据
    :param file: 存储数据路径以及文件名
    :param header: 文件header
    :return:
    """
    with open(file, 'ab+') as f:

        if header:
            f.write(header)
        f.writelines(rows)
