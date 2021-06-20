#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @File   : 008-two-sets.py
# @Date   : 2021/06/20
# @Author : Yuvv <yuvv_th@outlook.com>


def solve(n: int) -> (bool, list, list):
    n_sum = (n + 1) * n // 2
    if n_sum % 2 == 1:
        return False, None, None
    half_n_sum = n_sum // 2
    s1 = list()
    s2 = list()
    while n > 0:
        if n <= half_n_sum:
            s1.append(n)
            half_n_sum -= n
        else:
            s2.append(n)
        n -= 1
    return True, s1, s2


if __name__ == '__main__':
    num = int(input())
    r, s1, s2 = solve(num)
    if r:
        print('YES')
        print(len(s1))
        print(' '.join(map(str, s1)))
        print(len(s2))
        print(' '.join(map(str, s2)))
    else:
        print('NO')
