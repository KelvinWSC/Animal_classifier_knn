#%%
import pandas as pd

#%%
df = pd.read_csv('zoo.csv')
df = df.drop('animal_name', axis=1)
df.info()
#%%
y = df['class_type']
x = df.drop('class_type', axis=1)
#%%
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=17)
#%%
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

for k in range(1,31):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    print(f'The accuracy of {k:2d} nearest neighbor(s): {metrics.accuracy_score(y_test, y_pred)*100:3.2f}%')

# %%
knn = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
knn.fit(x_train, y_train)

# %%
y_pred = knn.predict(x_test)
# %%
df_class = pd.read_csv('class.csv')
class_id = df_class[['Class_Number','Class_Type']].set_index('Class_Number').T.to_dict('list')
# %%
for i in range(5):
    print(f'row {i} is a {class_id[y_pred[i]][0]}')
