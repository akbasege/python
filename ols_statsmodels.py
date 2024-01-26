import pandas as pd
import statsmodels.api as sm

xls= pd.ExcelFile('abc.xlsx')

df1=pd.read_excel(xls, 'xyz')

y=df.iloc[:,3:]
X=df.iloc[:,:3]

X=sm.add_constant(X)

fit=sm.OLS(y,X).fit()

fit.summary()
