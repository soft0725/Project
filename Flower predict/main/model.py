from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import joblib
import numpy as np

# iris 데이터를 불러와서 dataset에 넣어준다.
dataset = datasets.load_iris() 

# 입력 데이터와 타깃을 준비한다.
X, y = dataset['data'], dataset['target']

# k - 최근접 이웃 알고리즘 사용 (이웃의 갯수는 3)
model = KNeighborsClassifier(n_neighbors=3)

# 모델 학습
model.fit(X, y)

# 학습시킨 모델을 파일로 저장
joblib.dump(model, './knn_model.pkl')
print("학습 끝")

load_model = joblib.load('./knn_model.pkl')

def predict(data):

    temp = np.array([data])
    X_new = temp.astype(np.float64)

    prediction = model.predict(X_new)

    result = dataset['target_names'][prediction]

    print(result)

    return result
