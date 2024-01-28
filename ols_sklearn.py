import pandas as pd
from sklearn.linear_model import LinearRegression



df=pd.read_csv('inflation interest unemployment.csv')

y=df['Unemployment, total (% of total labor force) (modeled ILO estimate)']
X=df['incomeLevel','Real interest rate (%)','Inflation, consumer prices (annual %)','adminregion']

reg=LinearRegression(fit_intercept=True).fit(X,y)

reg.score(X,y)
reg.intercept_
reg.coef_


