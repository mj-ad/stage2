# API Implementation
## Request methods and URL
| Method | URL | Description|
| ---- | ---- | ---- |
| GET | /api/user_id | Used to retrieve info on a paricular person. |
| POST | /api | Used to create new user input. |
| UPDATE | /api/user_id | Used to update a person's information |
| DELETE | /api/user_id | Used to delete a person's information. |

## HTTP Response Status Codes
| Code | Title | Description|
| ---- | ---- | ---- |
| 200 | OK | When a request was successful e.g when using GET or POST. |
| 400 | Bad Request | When a request is incorrect or could not be understood. |
| 404 | Not found | This occurs when the user id inputed does not exist

## API POST Format
This is an example of the layout to be posted.
```
{
        "name" : "Elon Musk"
}
```
When amount is negative it is an expense but when positive it is an income.

## API GET Format
This is an eample of the layout when a GET request is pushed
```
{
        "id": 1,
        "name": "Elon Musk",
    }
```