word_list = []
char_dic = {chr(i + 97): 0 for i in range(26)} # 文字 (a-z) の辞書、97 は 'a' の文字コード

# 英単語の入力を受け付ける
while True:
    buf = input('英単語を入力してください：')
    if buf:
        word_list.append(buf)
    else:
        # 何も入力されずに Enter を押されたらループを抜けて次の処理をする
        break

if word_list:  # word_list に一つ以上の単語が含まれている時だけこれらの処理をする
    word_list.sort()  # 並べ替える（ソート）
    print('入力した英単語：', word_list)

    # word_list に格納された各単語に対して、文字数をカウントする
    for word in word_list:
        for char in word:
            char_dic[char] += 1

    # char_dic に含まれている各文字に対して、カウントされた値を出力する
    for char in char_dic:  # この char は数行上の char とはスコープが違い、異なるものであることに注意
        count = char_dic[char]
        if count > 0:  # 辞書の値が 1 以上の時だけ出力する
            print(f'{char}が{count}個ありました')
