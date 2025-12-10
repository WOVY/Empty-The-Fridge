# 🥘 냉장고를 털어라 (Smart Recipe Finder)

> **COMP322 Introduction to Databases Term Project (Phase 4)**
> 사용자의 냉장고 속 재료를 기반으로 요리 가능한 레시피를 추천해주는 웹 애플리케이션입니다.

<br>

## 👨‍💻 Team Members (Team 4)

* **김환**
* **서한녕**
* **송재표**

<br>

## 🎥 Demo Video

본 애플리케이션의 주요 기능 시연 영상은 아래 이미지를 클릭하거나 링크를 통해 확인하실 수 있습니다.

[![Video Label](http://img.youtube.com/vi/Db9HRL8XI-I/0.jpg)](https://www.youtube.com/watch?v=Db9HRL8XI-I)

* **YouTube Link**: [https://www.youtube.com/watch?v=Db9HRL8XI-I](https://www.youtube.com/watch?v=Db9HRL8XI-I)

<br>

## 🛠 Development Environment

본 프로젝트는 아래 환경에서 개발 및 테스트되었습니다.

* **OS**: Windows 10 / 11 (64bit)
* **Language**: Python 3.12.x
* **Framework**: Flask
* **Database**: Oracle Database
* **DB Library**: oracledb (Thin mode)
* **Frontend**: HTML5, CSS
* **IDE**: Visual Studio Code

<br>

## 🚀 How to Run (실행 방법)

애플리케이션을 실행하기 전, 반드시 아래 절차를 따라 설정해 주세요.

### 1. 데이터베이스 테이블 생성
제공된 `sql` 파일을 Oracle DB에서 실행하여 테이블(`USER_T`, `RECIPE`, `INGREDIENT` 등)과 시퀀스를 생성합니다.

### 2. 프로젝트 설정 파일 수정 (`config.py`)
루트 디렉토리의 `config.example.py` 파일을 열어 **본인의 Oracle DB ID와 Password**로 수정한 후 파일 이름을 `config.py`로 수정합니다..

```python
import os

# Oracle DB 연결 정보 (사용자 환경에 맞게 수정 필수)
ORACLE_USER = "본인의_DB_ID"          # 예: SCOTT
ORACLE_PASSWORD = "본인의_DB_PASSWORD" # 예: TIGER
ORACLE_DSN = "localhost:1521/orcl"   # 호스트:포트/서비스명 (XE 버전 사용 시 localhost:1521/xe)

# Flask 세션 암호화 키
SECRET_KEY = "comp322_secret_key"
````

### 3\. 애플리케이션 실행

(필요한 라이브러리를 설치 후) Flask 서버를 실행합니다.

```bash
# 필요 라이브러리 설치 (예시)
pip install flask oracledb

# 서버 실행
python app.py
```

<br>

## 💡 Key Features (주요 기능)

### 1\. 🔐 사용자 인증 (Authentication)

  * **회원가입/로그인**: 세션(Session) 기반 인증을 통해 개인화된 서비스를 제공합니다.
  * **마이페이지**: 닉네임 및 비밀번호 변경, 회원 탈퇴(Cascade 삭제 적용) 기능을 제공합니다.

### 2\. 🥦 냉장고 파먹기 (Main Feature)

  * **재료 관리**: '나의 냉장고'에 현재 보유 중인 식재료를 추가하거나 삭제할 수 있습니다.
  * **레시피 추천**: 사용자가 가진 재료만으로 요리할 수 있는 레시피를 자동으로 필터링하여 추천합니다.

### 3\. 🔍 레시피 검색 및 상세 조회

  * **통합 검색**: 요리 이름, 작성자, 조리 방법(끓이기, 굽기 등), 요리 종류(국, 반찬 등) 등 다양한 조건으로 검색이 가능합니다.
  * **영양 정보 필터**: 칼로리, 탄수화물, 단백질 등의 최소/최대 범위를 지정하여 건강한 레시피를 찾을 수 있습니다.
  * **랭킹 시스템**: 메인 화면에서 실시간 반응을 반영한 '즐겨찾기 많은 순', '댓글 많은 순' Top 5 레시피를 확인할 수 있습니다.

### 4\. 💬 커뮤니티 및 관리 (CRUD)

  * **레시피 등록/수정/삭제**: 사용자는 나만의 레시피를 공유할 수 있으며, 본인이 작성한 글에 대해서만 수정 및 삭제 권한을 가집니다.
  * **상호작용**: 레시피에 댓글을 남기거나 즐겨찾기(찜) 기능을 통해 다른 사용자와 소통할 수 있습니다.

<!-- end list -->

```
```