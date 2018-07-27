# pattern 0
# 九九の表を表示する
for v in range(1, 10):
    for h in range(1, 10):
        print(f"{(v * h):3d}", end="")

    print("")

# pattern 1
# 九九のリストを作成する
table = [[(x * y) for y in range(1, 10)] for x in range(1, 10)]  # Lesson9 - 7. 二次元リスト でのリスト内法表記による二次元リストの作成例を参照

# 九九の表を表示する
for i in range(len(table)):
    for j in range(len(table[i])):
        print(f'{table[i][j]:3d}', end='')
    print('')  # 改行
