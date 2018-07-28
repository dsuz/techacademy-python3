# from numbers import fibonacci    # ディレクトリ構造に依存せず、同じディレクトリのモジュールを読み込むやり方
from exercise import numbers  # ディレクトリ構造に依存するので要注意

while True:
    try:
        n = int(input('何番目の数値を求めますか？：'))

        if n > 0:
            print(numbers.fibonacci(n))
        else:
            print('1以上の数を指定してください')
    except ValueError:
        print('不正な値です。終了します。')
        break

