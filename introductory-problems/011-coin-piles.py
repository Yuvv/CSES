#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @File   : 011-coin-piles.py
# @Date   : 2021/06/22
# @Author : Yuvv <yuvv_th@outlook.com>


def solve(a: int, b: int) -> bool:
    ab_sum = a + b
    if ab_sum % 3 != 0:
        return False

    while True:
        if a == b:
            return True
        elif a > b:
            diff = a - b
            a -= 2 * diff
            b -= diff
        else:
            diff = b - a
            a -= diff
            b -= 2 * diff
        if a == 0 and b == 0:
            return True
        elif a <= 0:
            return False
        elif b <= 0:
            return False
    return True


if __name__ == '__main__':
    cnt = int(input())
    for _ in range(cnt):
        a, b = map(int, input().split())
        if solve(a, b):
            print('YES')
        else:
            print('NO')
