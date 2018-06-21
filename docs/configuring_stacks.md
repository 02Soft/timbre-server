# Timbre 기술스택 정하기 - 백엔드

## 1. Django

## 2. Cloud Server

AWS, GCP, Azure, IBM Bluemix 등등 여러 클라우드 서비스가 있지만, 사람들이 가장 많이 쓰는 AWS와 Google Cloud Platform 만을 비교해본다.

그 중에서도, 비용 절감 차원에서 Serverless Computing 이 가능한 옵션을 알아보았는데,

- AWS Lambda
- GCP Cloud Function

이 두 가지가 있었지만, AWS Lambda는 파이썬 3.6 런타임을 지원하는 반면에 Cloud Function 은 아직 노드만 지원한다!

**결론 : AWS Lambda 를 사용하자**

## 3. Database

Django 는 기본 ORM 이 매우 잘 되어 있어, RDB를 사용하는 것이 매우 이득이다.  
MySQL, Postgres, 등등의 옵션이 많지만 기존 코드 베이스가 MySQL 기반이라 **MySQL 사용**

하지만, 테스트를 위한 `development` 환경에서는 **SQLITE 사용**,  
단, SQLITE에서 지원하지 않는 기능이 들어갈 때는 테스트 환경을 별도로 생성!