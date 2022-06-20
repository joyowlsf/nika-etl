# nika-etl

## 프로젝트 소개
패션 시장은 나날이 발전하고 거대해지고 있으며 새로운 브랜드가 많이 생기고 패션 트렌드가 빠르게 변화고 있습니다. 우리나라 사람들에 실시간 패션 트렌드를 분석하기 위해 유명한 패션 카페의 데이터를 수집하여 패션 트렌드를 분석합니다.

<p align="center"><img src="https://user-images.githubusercontent.com/36403696/174538748-0830ebe9-4ea9-45b1-8a78-8726b3a8cbb8.png"  width="600" height="400" />


Ubuntu 20.04 환경에서 프로젝트를 진행했습니다.

#### 1.파이썬을 활용하여 네이버 카페 게시물에 타이틀 제목 추출후 csv형태로 가공합니다.
#### 2.DW(Data Warehouse)인 몽고디비에 데이터를 적재합니다.
#### 3.적재된 데이터를 조회하여 형태소 단위로 데이터를 가공 및 분류 합니다.
#### 4.시각화를 위해 Data Mart인 엘라스틱서치에 가공한 데이터를 적재합니다.
#### 5.Kibana를 활용하여 데이터를 시각화 합니다.

## 요구사항

#### python
- version: 3.8.10

#### Airflow
- version: 2.1.2
- localhost:8080 

#### MongoDB
- version: 4.4.14
- localhost:27017

#### Elasticsearch
- version: 7.17.4
- localhost:9201

#### kibana
- version: 7.17.4
- localhost:5601

