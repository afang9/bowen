#/usr/bin/env python
# --*-- coding:utf-8 -*-
from kuangjia.report.tes_报告 import run_baogao
from kuangjia.data.read_数据 import read_runtes
if __name__=='__main__':
    mu=read_runtes()
    print(mu)
    if 'all' in mu:
        run_baogao('*')
    else:
        run_baogao(mu)
