"""
任意の長さのランダムなパスワードを生成し、出力するプログラムを作りましょう。
ランダムなパスワードは generate_password 関数に生成させ、それを呼び出すようにしましょう。

generate_password 関数の仕様は次の通りに作ってください。
1. 引数 length をとる。length は「生成するパスワードの長さ」とする
2. 戻り値は str で、生成したパスワードを返す
"""

import string
import random


def generate_password(length):
    """
    指定された長さのパスワードを生成する。

    Parameters
    ----------
    length : int
        パスワードの長さ

    Returns
    -------
    password: str
        生成されたパスワード文字列
    """
    # パスワードに使う文字を char_list として string.printable から一部を抜き出す。
    char_list = string.printable[0:94]  # string.printable の中にはスペースや改行コードなどパスワードに使うには不適切な文字も含まれているため。
    password = ''
    # パスワードを生成する
    for _ in range(length):
        index = random.randint(0, len(char_list) - 1)
        password = password + char_list[index]

    return password


while True:
    buf = input('Password generator. How long should your password be? :')
    try:
        password_length = int(buf)
        print(generate_password(password_length))
    except ValueError:
        print('invalid value.')
