def fibonacci(n):
    """
    フィボナッチ数を返す
    
    Parameters
    ----------
    n : int
        番
    
    Returns
    -------
    fibonacci number: int
        n 番目のフィボナッチ数
    """
    if n != int(n):
        return 0  # n に整数でないものが指定されたらエラーとする

    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 2) + fibonacci(n - 1)
    else:
        return 0  # n に 0 または負の整数が指定されたらエラーとする


if __name__ == '__main__':
    # テスト用コード
    print(fibonacci(8))
    print(fibonacci(9))
    print(fibonacci(10))
    print(fibonacci(-1))
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(1.5))
    print(fibonacci('a'))
