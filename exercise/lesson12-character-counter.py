word_list = []  # 単語リスト
char_dic = {chr(i + 97): 0 for i in range(26)} # 文字 (a-z) の辞書、97 は 'a' の文字コード

# 英単語の入力を受け付ける
while True:
    buf = input('英単語を入力してください：').lower()  # 念の為全部小文字にしておく

    if not buf:
        # 何も入力されずに Enter を押されたらループを抜けて次の処理をする
        break

    word_list.append(buf)  # 単語をリストに追加する
    for c in buf:
        char_dic[c] += 1  # 登場した文字をカウントアップする

if word_list:  # word_list に一つ以上の単語が含まれている時だけこれらの処理をする
    word_list.sort()  # 並べ替える（ソート）
    print('入力した英単語：', word_list)

    # char_dic に含まれている各文字に対して、カウントされた値を出力する
    for k, v in char_dic.items():  # k, v はそれぞれ key, value の短縮形で、文字とカウントされた値を表す
        if v > 0:  # 辞書の値が 1 以上の時だけ出力する
            print(f'{k}が{v}個ありました')
