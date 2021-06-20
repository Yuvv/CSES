#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @File   : 007-two-knights.py
# @Date   : 2021/06/20
# @Author : Yuvv <yuvv_th@outlook.com>


def solve(n: int) -> int:
    cell_count = n * n
    total = cell_count * (cell_count - 1)

    # corner: -4*2
    total -= 4 * 2
    # aside corner: -8*3
    total -= 8 * 3
    # aside aside corner: -(n-4)*4*4
    total -= (n - 4) * 4 * 4
    # -4*4
    total -= 4 * 4
    # -(n-4)*4*6
    total -= (n - 4) * 4 * 6
    # -(n-4)*(n-4)*8
    total -= (n - 4) * (n - 4) * 8
    return total // 2


if __name__ == '__main__':
    num = int(input())
    for i in range(1, num + 1):
        print(solve(i))
