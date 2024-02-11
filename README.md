# JWT_authentication
* first get the clone of project
* git clone https://github.com/souravojhaji/JWT_authentication/tree/source_code
* Instructions for run this project

* first create virtual environment and activate it

```
pip install python-dotenv
python -m venv venv
```

* for windows
```
.\venv\Scripts\activate
```

* for ubuntu
```
source venv/bin/activate
```

* for install requirements or depedencies
```
pip install -r requirements.txt
```
* for run this project
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
* api urls with payload
* for user registration
```
url: http://127.0.0.1:8000/api/v1/register/
payload --> 
{
    "email" : "b@gmail.com",
    "password" :"b"
}
```
* for user login
```
url: http://127.0.0.1:8000/api/v1/login/
payload --> 
{
    "email" : "b@gmail.com",
    "password" :"b"
}
```