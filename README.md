# Board API
작성자: [김범서](https://www.github.com/lemon-lime-honey/)

# 시연영상
[![시연영상](https://img.youtube.com/vi/h2mOZdoglTs/default.jpg)](https://youtu.be/h2mOZdoglTs)

# 실행
1. 프로젝트 루트 폴더에 `.env`파일을 생성하고 다음의 키를 추가한다.
  - `secret_key`: Django 프로젝트 `settings.py`의 `SECRET_KEY`에 들어가는 값
  - `db_host`: 데이터베이스 호스트 주소
  - `db_name`: 데이터베이스 이름
  - `db_user`: 데이터베이스 사용자의 계정명
  - `db_pw`: 데이터베이스 계정의 비밀번호
2. MySQL 서버 연결
3. `CREATE DATABASE db_name`
4. `python manage.py migrate`
5. `python manage.py runserver`

## 호출
| method | url | description |
| --- | --- | --- |
| POST | /accounts/signup/ | 회원가입 |
| POST | /accounts/token/ | 로그인 |
| GET | /posts/ | 게시글 목록 열람 |
| POST | /posts/ | 게시글 작성 |
| GET | /posts/<post_pk>/ | 게시글 열람 |
| PUT | /posts/<post_pk>/ | 게시글 수정 |
| DELETE | /posts/<post_pk>/ | 게시글 삭제 |


# ERD
![ERD](/images/ERD.png)

# API 명세
## accounts
### 가입 `POST` /accounts/signup/
<details>
<summary>Request parameters</summary>

| Parameter | Type | Description |
| --- | --- | --- |
| email | String | `(something)@(something)` 형식 |
| password | String | 최소 8자 |

</details>

<details>
<summary>Response</summary>

#### 200 OK
반환 값 없음

#### 400 Bad Request
- 이메일이나 비밀번호가 유효하지 않은 값일 경우

| Field | Message |
| --- | --- |
| email | Enter a valid email address. |
| password | Password must be longer than 7 letters |

- 중복된 이메일인 경우

| Field | Message |
| --- | --- |
| email | user with this email address already exists.|

</details>

<details>
<summary>암호화된 비밀번호</summary>

![password](/images/accounts.png)

</details>

### 로그인 `POST` /accounts/token/

<details>
<summary>Request parameters</summary>

| Parameter | Type | Description |
| --- | --- | --- |
| email | String | `(something)@(something)` 형식 |
| password | String | 최소 8자 |

</details>

<details>
<summary>Response</summary>

#### 200 OK
| Field | Type | Description |
| --- | --- | --- |
| refresh | String | refresh 토큰 |
| access | String | access 토큰 |

#### 400 Bad Request
- 이메일이나 비밀번호가 유효하지 않은 값일 경우

| Field | Message |
| --- | --- |
| email | Enter a valid email address. |
| password | Password must be longer than 7 letters |

</details>

## posts
### `GET` /posts/
<details>
<summary>Response</summary>

#### 200 OK
```
{
    "count": 50,
    "next": "http://localhost:8000/posts/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "test1"
        },
        {
            "id": 2,
            "title": "test2"
        },
        {
            "id": 3,
            "title": "test3"
        },
        {
            "id": 4,
            "title": "test4"
        },
        {
            "id": 5,
            "title": "test5"
        }
    ]
}
```

</details>

### `GET` /posts/<post_pk>/
<details>
<summary>Response</summary>

#### 200 OK
게시글이 존재할 때

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | 게시글 번호 |
| title | String | 게시글 제목 |
| content | String | 게시글 내용 |

#### 404 Not Found
게시글이 존재하지 않을 때

```
{
    "detail": "Not found."
}
```

</details>

### `POST` /posts/
<details>
<summary>Request parameters</summary>

| Parameter | Type | Description |
| --- | --- | --- |
| title | String | 게시글 제목 |
| content | String | 게시글 내용 |

</details>

<details>
<summary>Response</summary>

#### 200 OK
| Field | Type | Description |
| --- | --- | --- |
| id | Integer | 게시글 번호 |
| title | String | 게시글 제목 |
| content | String | 게시글 내용 |

#### 401 Unauthorized
로그인을 하지 않은 사용자가 글을 작성하려 했을 경우

```
{
    "detail": "Authentication credentials were not provided."
}
```

</details>

### `PUT` /posts/<post_pk>/
<details>
<summary>Request parameters</summary>

| Parameter | Type | Description |
| --- | --- | --- |
| title | String | 게시글 제목 |
| content | String | 게시글 내용 |

</details>

<details>
<summary>Response</summary>

#### 200 OK
게시글 작성자가 글을 수정하는 경우

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | 게시글 번호 |
| title | String | 게시글 제목 |
| content | String | 게시글 내용 |

#### 401 Unauthorized
로그인하지 않은 사용자가 글을 수정하려 한 경우

```
{
    "detail": "Authentication credentials were not provided."
}
```

#### 403 Forbidden
글을 작성하지 않은 사용자(로그인이 된 상태)가 글을 수정하려 한 경우

</details>

### `DELETE` /posts/<post_pk>/
<details>
<summary>Response</summary>

#### 204 No Content
게시글 작성자가 글을 삭제하는 경우

#### 401 Unauthorized
로그인하지 않은 사용자가 글을 삭제하려 한 경우

```
{
    "detail": "Authentication credentials were not provided."
}
```

#### 403 Forbidden
글을 작성하지 않은 사용자(로그인이 된 상태)가 글을 삭제하려 한 경우

</details>

# 구현
## 사용한 패키지
- `Django` 4.2.4
- `Django REST Framework` 3.14.0
- `Simple JWT` 5.2.2
- `MySQLClient` 2.2.0
- `python-dotenv`

## accounts
- `username`을 사용하지 않고 대신 `email`을 계정명으로 사용해야 하므로 사용자 정의 사용자 모델을 작성했다.
- 이때 이메일 필드에는 `unique=True`를 설정했다.
- Django의 기본 인증 시스템인 `django.contrib.auth.backends.ModelBackend`를 대체하기 위한 `EmailBackend`를 작성하였다.
- 로그인 시 JWT를 사용하기 위해 `Simple JWT` 패키지의 `TokenObtainPairSerializer`를 상속받아 시리얼라이저를 작성하였고, `TokenObtainPairView`를 상속한 뷰를 작성해 새로 작성한 시리얼라이저를 사용하게 했다.
- 이메일 주소와 비밀번호는 시리얼라이저에서 `.validate_{field}` 메서드를 구현해 유효성을 검사하게 하였다.

## posts
- Django REST Framework의 `ViewSet`과 `DefaultRouter`를 사용하였다.
- `ViewSet`을 사용하면 여러 뷰 함수를 작성하지 않아도 하나의 클래스에서 하나의 모델에 관한 동작 구현을 한 번에 할 수 있다는 점이 좋아 선택했다.
- `DefaultRouter` 또한 규칙에 따라 자동으로 URL을 할당하기 때문에 어떻게 URL을 정할지 고민하지 않아도 된다는 점에서 선택했다.
- `create`, `update`, `destroy`가 요구하는 권한과 `list`, `retrieve`가 요구하는 권한이 달라야 하므로 `.get_permissions(self)` 메서드를 재정의하였다.
- 비슷한 이유에서 `.get_serializer_class(self)` 메서드를 재정의하여 `list` 메서드와 그 외의 메서드가 사용하는 시리얼라이저의 종류를 다르게 했다.
- 게시글 생성에 성공했다면 `201 Created`, 목록 반환, 개별 게시글 열람, 수정에 성공했다면 `200 OK`, 삭제에 성공했다면 `204 No Content`, 로그인이 필요한 동작을 시도했을 때 로그인을 하지 않은 경우 `401 Unauthorized`, 로그인은 했으나 게시글 작성자가 아니라 수정, 삭제에 실패하는 경우 `403 Forbidden`을 반환한다.
- 시리얼라이저는 `list`에 사용되는 경우에만 `id`와 `title`필드, 그 외에는 `id`, `title`, `content` 필드가 포함되도록 하였다.