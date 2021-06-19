#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @File   : 001-weird-algorighm.py
# @Date   : 2021/06/19
# @Author : Yuvv <yuvv_th@outlook.com>


def solve(n):
    while n != 1:
        print(n, end=' ')
        if n % 2 == 1:
            n = n * 3 + 1
        else:
            n //= 2
    print(n)


if __name__ == '__main__':
    solve(int(input()))
