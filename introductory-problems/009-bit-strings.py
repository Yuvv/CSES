#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @File   : 009-bit-strings.py
# @Date   : 2021/06/20
# @Author : Yuvv <yuvv_th@outlook.com>


def solve(n: int) -> int:
    return 2**n % 1000000007


if __name__ == '__main__':
    num = int(input())
    print(solve(num))
