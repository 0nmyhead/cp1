# 코드스테이츠 CP1

코드스테이츠 AIB 커리어 프로젝트 1; DE - 프로젝트 입니다.

## Overview

- 구직자(혹은 수강생)에게 맞는 구인, 구직 활동을 위한 데이터 처리 모델을 위한 앱 입니다.
- ML용 데이터 수집이 목표입니다.
## Roadmap

- 주기적으로 구인 사이트([원티드](https://www.wanted.co.kr/) 등)에서 데이터 관련 직군의 구인 공고에서 요구 기술 스택 등을 스크래핑.
- 취합한 데이터 정제 후 Google Cloud Flatform(Firebase(1) or BigQuery(2))에 쓰기, 읽기.
- 해당 기능을 가진 GCP 인스턴스로 HTTP request에 따른 Autoscaling 가능한 Web API.
