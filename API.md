# GraphQl Documentation

GraphQL documentation can be accessed from the GraphiQL GUI on `/graphql` endpoint.

```
http://localhost:8000/graphql

```

GraphQL endpoint can be accessed at:

```
http://localhost:8000/
```

## General Queries

The following query will return logs information availabe in the local databse.

```
query{
  logs{
    id
    log
    user{
      username
    }
  }
}
```

To add the log you should be authenticated in the system.

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

`addLog` mutation requires user to be authenticated.

Example:

```
mutation{
  addLog(log: "I am having a nice day today!"){
    log{
      id
      log
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
