# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import os
import sys
f=open(r'.\D\D_input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可

from functools import lru_cache

n, a, b = [int(item) for item in input().split()]
total_comb = 0

@lru_cache(maxsize=None)
def my_comb(n, r):
    if r == 1:
        return n
    if n == 2:
        return 2   
    return my_comb(n-1, r-1) * n / r

total_comb -= my_comb(n, a)
total_comb -= my_comb(n, b)

# print(total_comb)

def bin(N):
    res = ''
    while N >= 2:
        if N == 2:
            res += '10'
        res += str(N%2)
        N = N//2

    return res[::-1]

temp_num = n - 1
temp_index = bin(temp_num)
# print(temp_index)
for i, v in enumerate(reversed(temp_index)):
    if v == '1':
        total_comb += my_comb(n + i, 2*i + 1)
    
    total_comb %= (10**9 + 7)


print(int(total_comb + 1))

