import pandas as pd
from sklearn.linear_model import LinearRegression

xls= pd.ExcelFile('abc.xlsx')

df1=pd.read_excel(xls, 'xyz')

y=df.iloc[:,3:]
X=df.iloc[:,:3]

reg=LinearRegression(fit_intercept=True).fit(X,y)

reg.score(X,y)
reg.intercept_
reg.coef_


