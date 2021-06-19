#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @File   : 003-repetitions.py
# @Date   : 2021/06/19
# @Author : Yuvv <yuvv_th@outlook.com>


def solve(dna_seq):
    s_len = len(dna_seq)
    i = 0
    j = 1
    mx_len = 1
    while j < s_len:
        while j < s_len and dna_seq[j] == dna_seq[i]:
            j += 1
        mx_len = max(mx_len, j - i)
        i = j
        j += 1

    return mx_len


if __name__ == '__main__':
    dna = input()
    print(solve(dna))
