#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @File   : 004-increasing-array.py
# @Date   : 2021/06/19
# @Author : Yuvv <yuvv_th@outlook.com>


def solve(numbers):
    n_len = len(numbers)
    cnt = 0
    for i in range(1, n_len):
        if numbers[i] < numbers[i - 1]:
            cnt += numbers[i - 1] - numbers[i]
            numbers[i] = numbers[i - 1]

    return cnt


if __name__ == '__main__':
    input()
    nums = list(map(int, input().split()))
    print(solve(nums))
