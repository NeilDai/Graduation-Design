import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def randomforest():
    # 数据处理
    df = pd.read_excel('Data01.xls')
    # 根据表头设置node
    X = df[
        ['Number of +consensus PRE', 'Number of -consensus PRE', 'Total consensus PRE', 'Number of +nonconsensus PRE',
         'Number of -nonconsensus PRE', 'Total nonconsensus PRE', 'Total PRE', 'promoter length/bp']]

    # 读取cluster作为Y
    df = pd.read_csv('Data.csv')
    Y = df['cluster'].values

    from sklearn.model_selection import StratifiedKFold

    KFolds = StratifiedKFold(n_splits=5)  # 5 fold
    fold_counter = 0
    result = []

    for train, test in KFolds.split(X, Y):
        fold_counter += 1
        print(f"fold #{fold_counter}")

        X_train, X_test, Y_train, Y_test = X.loc[train], X.loc[test], Y[train], Y[test]

        model = RandomForestClassifier(n_estimators=10, random_state=30)
        model.fit(X_train, Y_train)
        print(model.score(X_train, Y_train))
        print(model.score(X_test, Y_test))

        Y_score = model.predict(X_test)

        from sklearn import metrics

        print("准确度=", metrics.accuracy_score(Y_test, Y_score))

        feature_list = list(X.columns)
        feature_imp = pd.Series(model.feature_importances_, index=feature_list).sort_values(ascending=False)
        print(feature_imp)

        Y_score = pd.DataFrame(Y_score, columns=['Pred'])
        Y_test = pd.DataFrame(Y_test, columns=['Real'])
        Fold_result = pd.concat([Y_test, Y_score], axis=1)
        result.append(Fold_result)

    RF_result = pd.concat(result, axis=0)
    RF_result.to_csv('RF_result.csv')

    import Igem_Sub_ROC as roc
    roc.ROC('RF_result.csv', 'Random Forest')











