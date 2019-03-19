# breast_cancer_wisconsin_data.csv を取り込む（命令を追記すること）
import pandas as pd
cancer = pd.read_csv("breast_cancer_wisconsin_data.csv")

# 先頭の5行のみ表示する（命令を追記すること）
cancer.head()
cancer.info()

# X と y を作成する（命令を追記すること）
import numpy as np
# X = np.array(cancer.radius_mean)
x_temp = cancer.drop(["diagnosis"], axis=1)
X = (x_temp - np.min(x_temp)) / (np.max(x_temp) - np.min(x_temp)).values
print(X.shape)
X.head()
# y = np.array(cancer.diagnosis)
y = cancer.diagnosis.values

# カテゴリの数値化
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit(["B", "M"])                         # 良性：0, 悪性：1
y = le.transform(y.flatten())

# 数値化した状態を確認してみる
print(y)

# 訓練データ8割、テストデータ2割に分割する（命令を追記すること）
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2)

# ロジスティック回帰の回帰モデルを作成する
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


# 訓練データを回帰モデルに設定する（命令を追記すること）
model.fit(X_train, y_train)

