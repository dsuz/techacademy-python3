from lessons.baseball_team import Baseball_Team

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

# チーム名のアルファベット順に出力する
print('team        win lose draw   rate')
team_list.sort(key=lambda t: t.name)
for team in team_list:
    team.show_team_result()

# 負け数が多い順に出力する
print('team        win lose draw   rate')
team_list.sort(key=lambda t: t.lose, reverse=True)
for team in team_list:
    team.show_team_result()

