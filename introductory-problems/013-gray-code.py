#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @File   : 013-gray-code.py
# @Date   : 2021/06/22
# @Author : Yuvv <yuvv_th@outlook.com>

from typing import List


def solve(n: int) -> List[str]:
    count = 2**n
    result = []
    result.append('0' * n)
    for i in range(1, count):
        if i % 2 == 0:
            # change the left of first '1' from right
            r1_idx = result[i - 1].rfind('1')
            if result[i - 1][r1_idx - 1] == '0':
                result.append(result[i - 1][:r1_idx - 1] + '1' + result[i - 1][r1_idx:])
            else:
                result.append(result[i - 1][:r1_idx - 1] + '0' + result[i - 1][r1_idx:])
        else:
            # change the right one
            if result[i - 1][-1] == '0':
                result.append(result[i - 1][:-1] + '1')
            else:
                result.append(result[i - 1][:-1] + '0')
    return result


if __name__ == '__main__':
    num = int(input())
    result = solve(num)
    for e in result:
        print(e)
