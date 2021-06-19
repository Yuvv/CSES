#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @File   : 002-missing-number.py
# @Date   : 2021/06/19
# @Author : Yuvv <yuvv_th@outlook.com>


def solve(cnt, numbers):
    return cnt * (cnt + 1) // 2 - sum(numbers)


if __name__ == '__main__':
    cnt = int(input())
    nums = map(int, input().split())
    print(solve(cnt, nums))
