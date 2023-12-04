import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

def sort_dataset(dataset_df):
	#TODO: Implement this function
	#해당 년도를 기준으로 오름차순 정리
	return dataset_df.sort_values(by='year')

def split_dataset(dataset_df):
	#TODO: Implement this function
	#라벨 값에 0.001 곱하기
  dataset_df['salary'] = dataset_df['salary'] * 0.001
	#데이터에서 라벨(정답) 제거
  X = dataset_df.drop(columns='salary', axis=1)
	#라벨(정답) 모음
  Y = dataset_df['salary']
	#훈련, 테스트 데이터셋 분리
  X_train = X.iloc[:1718]
  X_test = X.iloc[1718:]
  Y_train = Y.iloc[:1718]
  Y_test = Y.iloc[1718:]

  return X_train, X_test, Y_train, Y_test

def extract_numerical_cols(dataset_df):
	#TODO: Implement this function
	#해당 column 있는 줄만 추출(dataframe을 빈환하기 위해 [[]] 사용)
	return dataset_df[['age', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'fly', 'war']]


def train_predict_decision_tree(X_train, Y_train, X_test):
	#TODO: Implement this function
	#DecisionTreeRegressor모델 객체 성성
	model = DecisionTreeRegressor()
 #모델 학습
	model.fit(X_train, Y_train)
 #훈련데이터 기준 예측 값 return
	return model.predict(X_test)

def train_predict_random_forest(X_train, Y_train, X_test):
	#TODO: Implement this function
	#RandomForestRegressor모델 객체 생성
	model = RandomForestRegressor()
 #모델 학습
	model.fit(X_train, Y_train)
 #훈련데이터 기준 예측 값 return
	return model.predict(X_test)

def train_predict_svm(X_train, Y_train, X_test):
	#TODO: Implement this function
	#standard scalar와 svm 모델 파이프 라인 생성(정규화 후 swm 학습을 위해)
	svm_pipe = make_pipeline(
			StandardScaler(),
			SVR()
	 )
 #모델 학습
	svm_pipe.fit(X_train, Y_train)
  #훈련데이터 기준 예측 값 return
	return svm_pipe.predict(X_test)

def calculate_RMSE(labels, predictions):
	#TODO: Implement this function
	#RMSE 계산 후 return
	return np.sqrt(np.mean((predictions-labels)**2))


if __name__=='__main__':
	#DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
	data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

	sorted_df = sort_dataset(data_df)
	X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)

	X_train = extract_numerical_cols(X_train)
	X_test = extract_numerical_cols(X_test)

	dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
	rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
	svm_predictions = train_predict_svm(X_train, Y_train, X_test)

	print ("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))
	print ("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))
	print ("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))