"""
Lesson 14 の課題で定義した Baseball_Team クラスを使います。
team_list として以下のように順不同に定義してください。

team_list = [
    Baseball_Team('Dragons', 59, 79, 5),
    Baseball_Team('Swallows', 45, 96, 2),
    Baseball_Team('Carp', 88, 51, 4),
    Baseball_Team('Giants', 72, 68, 3),
    Baseball_Team('Tigers', 78, 61, 4),
    Baseball_Team('BayStars', 73, 65, 5),
]

Lesson 14 の要領で表を出力してください。その時、以下の条件の表を出力してください。

・チーム名のアルファベット順
・負け数が多い順

次に、Baseball_Team クラスに rate プロパティを追加し、このプロパティから勝率を取得できるようにしてください。
rate プロパティを利用して、次の条件の表を出力してください。

・勝率が高い順（勝ち数が多い順ではないことに注意）

[ヒント]
やり方がわからない場合は、まずは以下のヒントからどのような言葉で検索したらよいか考えて調べてみましょう。

1. リストの要素の順番を並べ替えることを「ソート」と言います。
2. リストをソートするには sorted() 関数またはリストの sort() メソッドを使います。
3. ソートする時の基準となる項目をソートキー (key) と言います。
例えば、勝ち数が多い/少ない順に並べ替える時のソートキーは Baseball_Team クラスの win プロパティです。
4. ソートキーとして要素のプロパティを指定したい時には、ラムダ (lambda) を使って指定することができます。
5. クラスに読み取り専用のプロパティを追加したい時には @property というキーワードを使います。このキーワードは decorator と呼ばれます。
"""

class Baseball_Team:
    name = ''
    win = 0
    lose = 0
    draw = 0

    @property
    def rate(self):
        return self.calc_win_rate()

    def __init__(self, name, win, lose, draw):
        self.name = name
        self.win = win
        self.lose = lose
        self.draw = draw

    def calc_win_rate(self):
        return self.win / (self.win + self.lose)

    def show_team_result(self):
        print(f'{self.name:10}{self.win:5d}{self.lose:5d}{self.draw:5d}{self.calc_win_rate():8.3f}')


team_list = [
    Baseball_Team('Dragons', 59, 79, 5),
    Baseball_Team('Swallows', 45, 96, 2),
    Baseball_Team('Carp', 88, 51, 4),
    Baseball_Team('Giants', 72, 68, 3),
    Baseball_Team('Tigers', 78, 61, 4),
    Baseball_Team('BayStars', 73, 65, 5),
]

# チーム名のアルファベット順に出力する
print('team        win lose draw   rate', 'アルファベット順')
team_list.sort(key=lambda t: t.name)
for team in team_list:
    team.show_team_result()

# 負け数が多い順に出力する
print('team        win lose draw   rate', '負け数が多い順')
team_list.sort(key=lambda t: t.lose, reverse=True)
for team in team_list:
    team.show_team_result()

# 勝率が高い順に出力する
print('team        win lose draw   rate', '勝率が高い順')
team_list.sort(key=lambda t: t.rate, reverse=True)
for team in team_list:
    team.show_team_result()
