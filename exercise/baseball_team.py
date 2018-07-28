class Baseball_Team:
    name = ''
    win = 0
    lose = 0
    draw = 0

    def __init__(self, name, win, lose, draw):
        self.name = name
        self.win = win
        self.lose = lose
        self.draw = draw

    def calc_win_rate(self):
        return self.win / (self.win + self.lose)

    def show_team_result(self):
        print(f'{self.name:10}{self.win:5d}{self.lose:5d}{self.draw:5d}{self.calc_win_rate():8.3f}')


if __name__ == '__main__':
    # テスト用コード
    yb = Baseball_Team('BayStars', 73, 65, 5)
    print(yb.calc_win_rate())
    yb.show_team_result()
