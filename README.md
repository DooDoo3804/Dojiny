# 명세



## 1. 개요

- 프로젝트명 : Dojiny
- 개발인원 : 2명
- 개발 기간 : 2022.11.14 ~ 2022.11.24
- 주요 기능
  - 감독 hebind - CRUD 기능 , 구독, 좋아요
  - 영화 검색 - 장르/키워드 검색
  - 영화 추천
  - 사용자 - 팔로우, 회원가입 및 로그인, 회원 정보 수정, 유효성 검사 및 중복 검사
- 개발 언어 : Python JavaScript
- 개발 환경 : VSCode Django Node.js
- 데이터 베이스 : Django
- 형상 관리 툴 : GitHub
- ERD 툴 : draw.io
- 와이어 프레임 툴 : Figma



## 2. 페이지 기능 별 요구사항

#### 1. 회원가입 페이지

- 유효성 검사
  - 각 형식에 맞는 패턴 확인

- 중복확인 
  - 닉네임 / 이메일 / 유저아이디 중복검사

#### 2. 로그인 페이지

- 로그인이 필요한 페이지
  - behind, 영화 추천, 마이 페이지

- 로그인 검사
  - 아이디와 비밀번호가 일치하지 않으면 "이이디 또는 비밀번호가 일치하지 않습니다." 띄우기
  - 이외의 에러 처리
  - behind 작성을 위한 인증 관련 문구를 띄워줌
    - 주어진 email로 해당 정보/파일을 받음
  - 로그인 이후 메이 페이지 이동

#### 3. 영화 검색

- 로그인이 진행되지 않아도 검색 기능 가능
- 장르와 년도를 선택하는 것으로 영화 분류하여 선택 가능
- 정렬 기능

#### 4. Behind 페이지

- Behind
  - CRUD
  - behind 작성 권한이 있는 user만 작성 가능
  - 내용 수정을 해당 작성자만 가능
  - 해당 작성자를 팔로우 하는 기능
- Behind 댓글
  - CRUD
  - 모든 유저가 작성 가능
  - 내용이 비어있으면 작성 불가
  - 내용 수정을 해당 작성자만 가능
  - behind글 삭제 시 해당 댓글들도 삭제됨

#### 5. 영화 추천 페이지

- 내가 평가한(좋아요 누른) 영화를 바탕으로 영화 추천
- 호버시 영화 디테일 보여주기

#### 6. 마이 페이지

- 



## 3.  MVC 구조도





## 4. API 구성

| 기능                 | method     | url                      | return page                                         |
| :------------------- | ---------- | ------------------------ | --------------------------------------------------- |
| _**로그인 기능**_    | -          | -                        | -                                                   |
| 로그인 화면          | get        | /accounts/login/         | 로그인 페이지                                       |
| 로그인               | post       | /accounts/login/         | 메인페이지                                          |
| 로그아웃             | get        | /accounts/logout/        | 초기 화면                                           |
| 회원 가입            | get/post   | /accounts/signup/        | (성공시) 메인 페이지, (실패시) 회원 가입 페이지     |
| 비밀번호 수정        | post       | /accounts/password/      | (성공시) 메인 페이지, (실패시) 비밀번호 수정 페이지 |
| 회원 정보 페이지     | get        | /accounts/profile/       | 회원 정보 프로필                                    |
| 회원 정보 수정       | post       | /accounts/update/        | (성공시) 메인 페이지, (실패시) 정보 수정 페이지     |
| 회원 정보 삭제       | post       | /accounts/delete/        | 초기 화면                                           |
| _**감독 behind**_    | -          | -                        | -                                                   |
| behind 화면          | get        | /behinds/                | behind 페이지                                       |
| behind 작성          | post       | /behinds/create/         | behind 페이지                                       |
| behind 디테일        | get        | /behinds/detail/         | behind 디테일 페이지                                |
| behind 삭제          | post       | /behinds/delete/         | (성공 후) behind 페이지                             |
| behind 수정          | post       | /behinds/update/         | (성공 후) 디테일 페이지                             |
| comment 작성 및 수정 | get / post | /behinds/comment_create/ | (성공 후) 디테일 페이지                             |
| behind likes         | get        | /behinds/likes/          | (토글) behind 페이지                                |
| _**영화 추천**_      | -          | -                        | -                                                   |
| 추천 페이지          | get        | /recommandations/        | 추천 페이지                                         |
| _**영화 검색**_      | -          | -                        | -                                                   |
| 검색 메인 페이지     | get        | /movies/                 | 검색 메인 페이지                                    |
| 영화 디테일          | get        | /movies/detail/          | 영화 디테일 페이지                                  |
| _**마이 페이지**_    | -          | -                        | -                                                   |
|                      |            |                          |                                                     |



## 5. ERD 구조

![image-20221115122450677](C:\Users\multicampus\Desktop\Dojiny\README.assets\image-20221115122450677.png)



## 6. 와이어 프레임



