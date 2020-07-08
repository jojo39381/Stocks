import quandl
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split


df = quandl.get("WIKI/GOOGL")

print(df.head())
df = df[['Adj. Close']]

forecast_out = 1000

df['Prediction'] = df[['Adj. Close']].shift(-forecast_out)

print(df.tail())

X = np.array(df.drop(['Prediction'],1))

X = X[:-forecast_out]


y = np.array(df['Prediction'])

y = y[:-forecast_out]

x_train,
x_test,
y_train,
y_test = train_test_split(X, y, test_size=0.2)

svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_rbf.fit(x_train, y_train)

svm_confidence = svr_rbf.score(x_test, y_test)
print("svm confidence: ", svm_confidence)

lr = LinearRegression()

lr.fit(x_train, y_train)

lr_confidence = lr.score(x_test, y_test)
print("lr confidence: ", lr_confidence)

x_forecast = np.array(df.drop(['Prediction'],1))[-forecast_out:]


lr_prediction = lr.predict(x_forecast)


svm_prediction = svr_rbf.predict(x_forecast)
print(svm_prediction)

