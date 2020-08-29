import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve


def plot_learning_curve(estimator, title, X, y, axes=None, ylim=None, cv=None,
                        n_jobs=None, train_sizes=np.linspace(.1, 1.0, 5)):
    plt.figure(figsize=(4,3))
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")


    train_sizes, train_scores, test_scores, fit_times, _ = \
        learning_curve(estimator, X, y, cv=cv, n_jobs=n_jobs,
                       train_sizes=train_sizes,
                       return_times=True)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    fit_times_mean = np.mean(fit_times, axis=1)
    fit_times_std = np.std(fit_times, axis=1)

    # Plot learning curve
    plt.grid()
    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                         train_scores_mean + train_scores_std, alpha=0.1,
                         color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                         test_scores_mean + test_scores_std, alpha=0.1,
                         color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
                 label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
                 label="Cross-validation score")
    plt.legend(loc="best")
    return plt

# import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score


data = pd.read_csv(r'datasets\diabetes.csv') #資料集
#print(data.shape)
#print(data.columns)
#print(data.groupby('Outcome').size())

X = data.iloc[:, 0:8]  #八個特徵欄的資料
Y = data.iloc[:, 8]    #結果欄資料

models = []  #準備放置多個候選模型
models.append(("KNN", KNeighborsClassifier(n_neighbors=3))) #一般
models.append(("KNN-W", KNeighborsClassifier(n_neighbors=3, weights="distance"))) #距離越遠權重越低


#把原始資料分成訓練與測試(80/20)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
results = []
for name, model in models:
    model.fit(X_train, Y_train)
    results.append((name, model.score(X_test, Y_test)))
print('Training Test')
for i in range(len(results)):
    print("name: {}; score: {}".format(results[i][0],results[i][1]))
print('')



#交叉驗證評估
results = []
for name, model in models:
    kfold = KFold(n_splits=10) # K折交叉驗證器，將資料折成10份(9份訓練, 1份測試)
    cv_result = cross_val_score(model, X, Y, cv=kfold) #交叉驗證評估分數
    results.append((name, cv_result))
print('Cross Validation')
for i in range(len(results)):
    print("name: {}; cross val score: {}".format(results[i][0],results[i][1].mean()))

#繪製學習曲線圖
from sklearn.model_selection import ShuffleSplit


knn = models[0][1]   #KNeighborsClassifier(n_neighbors=3)
cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)

plt_learn = plot_learning_curve(knn, "Learn Curve for KNN Diabetes",
                    X, Y, ylim=(0., 1.2), cv=cv)

#挑出兩個最佳特徵
from sklearn.feature_selection import SelectKBest

selector = SelectKBest(k=2)
X_new = selector.fit_transform(X, Y)
print(X_new[0:5]) #列出出五筆

#最相佳特徵分別為 Glucose（血糖濃度）和 BMI指數
results = []
for name, model in models:
    kfold = KFold(n_splits=10)
    cv_result = cross_val_score(model, X_new, Y, cv=kfold)
    results.append((name, cv_result))
for i in range(len(results)):
    print("name: {}; cross val score: {}".format(
        results[i][0],results[i][1].mean()))

#繪製最佳特徵資料散布圖
plt.figure(figsize=(10, 6))
plt.ylabel("BMI")
plt.xlabel("Glucose")
plt.scatter(X_new[Y==0][:, 0], X_new[Y==0][:, 1], c='g', s=20, marker='o');  #陰性
plt.scatter(X_new[Y==1][:, 0], X_new[Y==1][:, 1], c='r', s=20, marker='^');  #陽性

plt.show()







