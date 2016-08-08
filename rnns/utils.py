# -*- coding:utf-8 -*-
__author__ = 'EricDoug'
import requests

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


def downloadfileByurl(url, file):
    """
    从url下载文件
    :param url: url地址
    :param file: 存储文件地址
    :return:
    """

    res = requests.get(url)
    res.raise_for_status()

    with open(file, 'wb') as f:
        for chunk in res.iter_content(100000):
            f.write(chunk)