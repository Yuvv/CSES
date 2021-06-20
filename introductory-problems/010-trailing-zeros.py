#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @File   : 010-trailing-zeros.py
# @Date   : 2021/06/20
# @Author : Yuvv <yuvv_th@outlook.com>


def solve(n: int) -> int:
    total = 0
    base = 5
    k = 1
    while k > 0:
        k = n // base
        total += k
        base *= 5
    return total


if __name__ == '__main__':
    num = int(input())
    print(solve(num))
