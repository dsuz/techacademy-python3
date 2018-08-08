# pattern 1: 課題の仕様の条件をそのまま実装するやり方
# ただし、100 までなら問題ないが、このやり方では素数を判定する範囲が大きくなると正しい結果を得られない
print('pattern 1')
for i in range(2, 101):
    if i != 2 and i % 2 == 0:
        continue
    if i != 3 and i % 3 == 0:
        continue
    if i != 5 and i % 5 == 0:
        continue
    if i != 7 and i % 7 == 0:
        continue
    print(i)

# pattern 2: Python の特徴に沿って短く書くやり方。ただし、計算には無駄が多い。
print('pattern 2')
for n in range(2, 101):
    for p in range(2, n):
        if n % p == 0:
            break
    else:
        print(n)

# pattern 3: 奇数のみに対して判定処理を行う
# 計算の回数が少なくて済む
print('pattern 3')
for n in range(1, 101):
    if n == 2:  # 2は自明な素数として処理する
        print(n)
    elif n % 2 != 0 and n > 2:  # 3以上の奇数に対して素数かどうか判定する
        odd = 3  # odd は奇数
        while odd**2 <= n:
            if n % odd == 0:
                break
            odd += 2  # odd を次の奇数にする
        else:
            print(n)
