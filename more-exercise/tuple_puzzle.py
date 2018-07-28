"""
word_list = ['foo', 'bar', 'baz']
というリストがあるとします。ここから、zip(), range(), list() 関数を使って以下の出力を得てください。
[(1, 'foo'), (2, 'bar'), (3, 'baz')]

[条件]
word_list = ['foo', 'bar', 'baz', 'qux']
に変更した時、それ以外の行を一切変更せずに次の出力が得られるように作ってください。
[(1, 'foo'), (2, 'bar'), (3, 'baz'), (4, 'qux')]

zip(), range(), list() を必ず使ってください。

while, for, if は使わないでください。

[その他]
(a, b) はタプルを表します。[a, b, c, ...] はリストを表します。つまり、[(1, 'foo'), (2, 'bar'), (3, 'baz')] は「タプルのリスト」を表しています。
"""
word_list = ['foo', 'bar', 'baz']

result = zip(range(1, len(word_list) + 1), word_list)
print(list(result))
