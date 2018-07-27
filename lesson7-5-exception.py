try:
    a = int(input("割られる数を入力してください："))
    b = int(input("割る数を入力してください："))
    c = a / b
    print(f"{a} ÷ {b} = {c}")
except ValueError:
    print('エラー：数値を入力してください')
except ZeroDivisionError:
    print('エラー：0で割り算しないでください')

print("処理を終了します")
