try:
    a = int(input("割られる数を入力してください："))
    b = int(input("割る数を入力してください："))
    c = a / b
except ValueError:
    print('エラー：数値を入力してください')
except ZeroDivisionError:
    print('エラー：0で割り算しないでください')
except:
    print("エラー：何らかのエラーが発生しました")
else:
    print(f"{a} ÷ {b} = {c}")
finally:
    print("処理を終了します")