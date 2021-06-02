# home-test

## Start Services

To start the services on WSL2 or Linux machine:

```bash
docker-compose up -d
```

# API Documentation

## Get orders for specific user from customer-facing service


| Method | Path             |
| :----- | :--------------- |
| `GET` | `/getAllUsersOrders?username=<username>` |

### Parameters

- `username` `(string: <required>)` – The username of user

### Sample Request

```bash
$ curl http://localhost:5050/getAllUsersOrders?username=test
```

## Add new order 


| Method | Path             |
| :----- | :--------------- |
| `POST` | `/buy` |

### Parameters

- `username` `(string: <required>)` – The username of user
- `userid` `(string: <required>)` – The id of the user
- `price` `(float: <required>)` – The price of the item 

### Sample Payload

```json
{
    "username": "test",
    "userid": "12322323",
    "price": 5002
}
```

### Sample Request

```bash
$ curl \
    --header "Content-Type: application/json" \
    --request POST \
    --data @payload.json \ 
    http://localhost:5050/buy
```
