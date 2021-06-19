#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @File   : 005-permutations.py
# @Date   : 2021/06/19
# @Author : Yuvv <yuvv_th@outlook.com>


def solve(n):
    if n <= 3 and n != 1:
        return None
    odd = [e for e in range(1, n + 1, 2)]
    even = [e for e in range(2, n + 1, 2)]
    even.extend(odd)
    return even


if __name__ == '__main__':
    result = solve(int(input()))
    if result:
        print(' '.join(map(str, result)))
    else:
        print('NO SOLUTION')
