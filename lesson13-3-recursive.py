import numbers

while True:
    n = int(input('何番目の数値を求めますか？：'))
    if n > 0:
        print(numbers.fibonacci(n))
    else:
        print('1以上の数を指定してください')
