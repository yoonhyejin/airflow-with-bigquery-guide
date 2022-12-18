# Set up

## Set up airflow
테스트 목적을 위해 이 가이드에서는 로컬에서 간단히 test airflow 를 띄우는 방법을 소개한다. 이미 에어플로우가 클라우드 환경에 띄워져있다면 이 부분을 스킵한다. 

## Create table
Raw data source 가 될 테이블을 만든다. 다음과 같이 dummy data 를 생성한다. (테스트 데이터는 github repository를 참고해라. )

## 기본 계정 및 권한 설정
Airflow Dag가 bigquery 에서 데이터를 가져오고 적재할수 있기 위해서 해당 권한을 가진 계정이 필요하다. ~~으로 발급받는다.