counter = 0  # 人数のカウンター
score_sum = 0  # 点数の合計
while True:
    score = int(input('点数を入力してください：'))
    if score < 0:
        break
    counter += 1
    score_sum += score

if counter > 0:  # 一人も入力されていない時は処理しない
    score_average = score_sum / counter  # 平均値
    print(counter, '人のテストの平均点は', score_average, '点です')
else:
    print('集計できません')
