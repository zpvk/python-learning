# -*- coding: utf-8 -*-
# @Author: Rohan Kumara
# @Date:   2020-11-13 03:51:58
# @Last Modified by:   Rohan Kumara
# @Last Modified time: 2020-11-14 00:00:03

def count_substring(string, sub_string):
    return [string[i:i+len(sub_string)] for i in range(len(string))].count(sub_string)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    p rint("",count)

