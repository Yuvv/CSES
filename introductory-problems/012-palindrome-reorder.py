#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @File   : 012-palindrome-reorder.py
# @Date   : 2021/06/22
# @Author : Yuvv <yuvv_th@outlook.com>


def solve(ss: str) -> str:
    ch_set = set()
    ch_list = list()
    for c in ss:
        if c not in ch_set:
            ch_set.add(c)
        else:
            ch_list.append(c)
            ch_set.remove(c)

    ch_set_len = len(ch_set)
    mid_ch = ''
    if ch_set_len > 1:
        return 'NO SOLUTION'
    elif ch_set_len == 1:
        mid_ch = list(ch_set)[0]

    return ''.join(ch_list) + mid_ch + ''.join(ch_list[::-1])


def solve2(ss: str) -> str:
    ch_d = dict()
    for c in ss:
        ch_d[c] = ch_d.get(c, 0) + 1
    ch_list = list()
    mid_single_ch = ''
    for ch, cnt in ch_d.items():
        if cnt == 1:
            if mid_single_ch:
                return 'NO SOLUTION'
            else:
                mid_single_ch = ch
        else:
            ch_list.append(ch * cnt)

    return ''.join(ch_list) + mid_single_ch + ''.join(ch_list[::-1])


if __name__ == '__main__':
    print(solve(input()))
