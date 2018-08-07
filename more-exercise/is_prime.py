"""
ユーザー定義関数 is_prime() を作り、それを使って素数判定をするプログラムを作りましょう。
is_prime 関数の仕様は次の通りに作ってください。
1. 引数 n をとる。n は「素数判定の対象となる自然数」とする
2. 戻り値は bool で、n が素数の時 True を返す
"""


def is_prime(n):
    """
    与えられた数を素数であるか判定する。アルゴリズムは「エラトステネスのふるい」

    Parameters
    ----------
    n : int
        素数判定をする数

    Returns
    -------
    result: bool
        n が素数である時は True、合成数である時は False
    """
    # 自明なケースに対してはすぐ結果を返す
    # ここでは判定対象が 2 以下の数と偶数である時に自明なケースとする
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        print(n, 'is even.')
        return False

    # 自明でないケースに対して素数判定をする
    # ここでは 3 以上の奇数に対して判定をする
    odd = 3  # odd は奇数で 3, 5, 7, 9,... と大きくなる
    while odd**2 <= n:
        if n % odd == 0:  # 割り切れたらその時点で素数ではない
            print(odd, 'can divide', n)
            return False
        odd = odd + 2

    # 全ての odd で割り切れなかったら、素数である
    return True


while True:
    buf = input('input number for prime testing: ')

    if not buf:  # 何も入力がなければプログラムを終了する
        print('exit.')
        break

    try:
        input_number = int(buf)
        if is_prime(input_number):
            print(buf + ' is a prime number.')
        else:
            print(buf + ' is NOT a prime number.')
    except ValueError:
        print('invalid value.')
