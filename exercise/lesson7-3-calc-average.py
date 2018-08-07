score_list = []
while True:
    score = int(input('点数を入力してください：'))
    if score < 0:
        break
    score_list.append(score)

if score_list:
    score_average = sum(score_list) / len(score_list)
    print(len(score_list), '人のテストの平均点は', score_average, '点です')
else:
    print('集計できません')
