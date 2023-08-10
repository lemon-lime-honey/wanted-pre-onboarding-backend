# Board API
작성자: [김범서](https://www.github.com/lemon-lime-honey/)

# ERD
![ERD](/images/ERD.png)

# API 명세 및 구현
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