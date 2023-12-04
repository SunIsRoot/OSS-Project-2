import pandas as pd

#파일 불러오기
data = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

#문제 1

#2015~2018년도까지
for thisyear in [2015, 2016, 2017, 2018]:
  #해당 년도의
  year = data[data['year'] == thisyear]
  #H,avg, HR, OBR 분야에서의
  for activity in ['H', 'avg', 'HR', 'OBP']:
    print("\n{}년의 {}의 top 10 출력하기\n".format(thisyear,activity))
    # 해당 분야 점수의 내림차순 정렬하여 10개의 선수명과 분야 점수 출력
    print(year[['batter_name',activity]].sort_values(by=activity, ascending=False)[:10])

#문제 2
print("\n 2018년 각각의 포지션의 최고 높은 승리 기여도와 해당 플레이어 이름 출력하기\n")
#war에 대해서 내림차순 정렬
highwar = data[['cp','war','batter_name','year']].sort_values(by='war',ascending=False)
# 각각의 position들에 대하여
for position in ['포수', '1루수', '2루수', '3루수', '유격수', '좌익수', '중견수', '우익수']:
  #2018년도 이고 포지션이 해당 포시션일 때 1등 출력(위에서 war에 대해 내림차순 정렬을 해두어서 1등이면 자동으로 해당분야와 년도에서 war로 1등인 선수가 나온다.)
    highposition2018 = highwar[(highwar['year'] == 2018) & (highwar['cp'] == position)][:1]
    print(highposition2018);

#문제 3
print("\n Among R (득점), H (안타), HR (홈런), RBI (타점), SB (도루), \n war (승리 기여도), avg (타율), OBP(출루율), SLG (장타율) 중에 \n salary(연봉)과 연관 높은 것 출력하기\n")
#가장 높은 연관성 저장용
highestcorrelation = 0
#가장 높은 연관성을 가진 분야 저장용
highestact =""
#각각의 분야에 대해서
for act in ['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG']:
  #salary 항목과의 연관성 계산 후 저장
  returns = data['salary'].corr(data[act])
  #위에서 저장한 값을 가장 높은 연관성 저장용 변수와 비교하여 더 클 경우
  if highestcorrelation < returns:
    #해당 값 업로드
    highestcorrelation = returns
    #해당 분야 업로드
    highestact = act

print ("{}가 가장 연봉과 연관이 높습니다. ". format(highestact))