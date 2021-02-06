# Flask Authentication (JWT)

#### Use Technology
* Flask
* Migrate
* SQLAlchemy (ORM)
* werkzeug.security
* PostgreSQL
* Python 3

#### Requirements have all necessary library
```sh
Flask-JWT-Extended
Flask
Flask-SQLAlchemy
Flask-Migrate
Werkzeug
```

#### Installation and First Run
To use you need have local PostreSQL server and Database on name : User
```sh
$ python3 -m venv env
$ source env/bin/activate
$ https://github.com/Boryszs/flask-auth.git
$ cd flask-auth
$ pip install -r requirements.txt
$ flask run
$ Ctrl + C
$ flask db init     # use to create databse 
$ flask db migrate  # use to create databse
$ flask db upgrade  # use to create databse
```

#### Create table 
```sh 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password = db.Column(db.String(128))
```
 

#### Later you can run program
```sh
python3 app.py or flask run 
```

#### GET http://127.0.0.1:5000/  

return "Hello World"


![Zrzut ekranu z 2021-02-06 06-59-19](https://user-images.githubusercontent.com/62262900/107110645-c9a70680-6849-11eb-9e78-ac894a692934.png)


#### POST http://127.0.0.1:5000/register

```sh
"username":"username",
"password":"password"
```

#### POST http://127.0.0.1:5000/login

```sh
"username":"username",
"password":"password"
```

![Zrzut ekranu z 2021-02-06 06-58-43](https://user-images.githubusercontent.com/62262900/107110656-f3f8c400-6849-11eb-914d-f13dbe6be73e.png)


#### POST http://127.0.0.1:5000/protected
#### Header 

| KEY | VALUE |
| ------ | ------ |
| Authorization | Bearer return token on login  |
| Content-Type | application/json |

Successful access

![Zrzut ekranu z 2021-02-06 06-58-12](https://user-images.githubusercontent.com/62262900/107110662-0d9a0b80-684a-11eb-8cf7-881de8d06324.png)

Without access message

![Zrzut ekranu z 2021-02-06 07-02-55](https://user-images.githubusercontent.com/62262900/107110665-1f7bae80-684a-11eb-95ec-1f321d12869c.png)