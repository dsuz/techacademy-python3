# from baseball_team import Baseball_Team  # ディレクトリ構造に依存せず、同じディレクトリのモジュールを読み込むやり方
from exercise.baseball_team import Baseball_Team  # ディレクトリ構造に依存するので要注意

team_list = [
    Baseball_Team('Carp', 88, 51, 4),
    Baseball_Team('Tigers', 78, 61, 4),
    Baseball_Team('BayStars', 73, 65, 5),
    Baseball_Team('Giants', 72, 68, 3),
    Baseball_Team('Dragons', 59, 79, 5),
    Baseball_Team('Swallows', 45, 96, 2),
]

# そのまま出力する
print('team        win lose draw   rate')
for team in team_list:
    team.show_team_result()
