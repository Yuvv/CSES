#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @File   : 006-number-spiral.py
# @Date   : 2021/06/19
# @Author : Yuvv <yuvv_th@outlook.com>


def solve(r, c):
    if r >= c:
        if r % 2 == 1:
            return (r - 1)**2 + c
        else:
            return r**2 - c + 1
    else:
        if c % 2 == 1:
            return c**2 - r + 1
        else:
            return (c - 1)**2 + r


if __name__ == '__main__':
    cnt = int(input())
    for i in range(cnt):
        y, x = input().split()
        print(solve(int(y), int(x)))
