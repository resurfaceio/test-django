# GraphQl Documentation


GraphQL endpoint can be accessed at:

```
http://localhost
```

## General Queries

The following query will return news information availabe in the local databse.

```
query{
  allNews{
    id
    title
    user{
      username
    }
  }
}
```
Get news by ID:

```
query{
  newsById(id: "1"){
    id
    title
    user{
      username
    }
  }
}
```

To add the news you should be authenticated in the system.

## Auth required Mutations

You can create user using `createUser` mutation.

Example:

```
mutation{
 tokenAuth(username: "anyesh", password: "123456"){
  token
}
}
```

This will return a JWT token which you can attach in the headers for every GQL request.

```
AUTHORIZATION: "JWT <token here>
```

View loggedin user info:

```
query{
  user{
    username
    id
    isSuperuser
  }
}
```

`addNews` mutation requires user to be authenticated.

Example:

```
mutation{
  addNews(title: "This is a great short news!", body: "body here"){
    news{
      id
      title
      user{
          username
      }
    }
  }
}

```

## Error handling

Error in GQL gives 200 HTTP status code so we have to always to look for `errors` key in the response to check if the request succeed or failed.

Example Error:

```
{
  "errors": [
    {
      "message": "You are not logged in",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": [
        "user"
      ]
    }
  ],
  "data": {
    "user": null
  }
}


```
