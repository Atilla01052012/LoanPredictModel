import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

df=pd.read_csv("loan.csv")

df = df.drop(columns=['Loan_ID'])

for i in df.columns :
    if df[i].isnull().sum() > 0 :
        df[i] = df[i].fillna(df[i].mode()[0])

df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
df['Married'] = df['Married'].map({'Yes': 1, 'No': 0})
df['Education'] = df['Education'].map({'Graduate': 1, 'Not Graduate': 0})
df['Dependents'] = df['Dependents'].map({'0': 0, '1': 1, '2': 2, '3+': 3})
df['Self_Employed'] = df['Self_Employed'].map({'Yes': 1, 'No': 0})
df['Property_Area'] = df['Property_Area'].map({'Urban': 1, 'Rural': 0, 'Semiurban': 2})
df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})


x=df.drop('Loan_Status', axis=1)
y=df['Loan_Status']

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

dt = DecisionTreeClassifier( 
    criterion='entropy',
    max_depth=5,
    min_samples_split=10
)
model = dt.fit(x_train,y_train)

with open('model.pkl','wb') as f :
    pickle.dump(model,f)