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


![Zrzut ekranu z 2021-02-06 06-59-19](https://user-images.githubusercontent.com/62262900/107112173-d29dd500-6855-11eb-9e7d-429ca49d6c62.png)


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

![Zrzut ekranu z 2021-02-06 06-58-43](https://user-images.githubusercontent.com/62262900/107112187-f3662a80-6855-11eb-92e9-4780ae8f383f.png)


#### POST http://127.0.0.1:5000/protected
#### Header 

| KEY | VALUE |
| ------ | ------ |
| Authorization | Bearer return token on login  |
| Content-Type | application/json |

Successful access

![Zrzut ekranu z 2021-02-06 08-34-50](https://user-images.githubusercontent.com/62262900/107112247-72f3f980-6856-11eb-87ca-046704028b6d.png)

Without access message when token will expire

![Zrzut ekranu z 2021-02-06 07-02-55](https://user-images.githubusercontent.com/62262900/107112307-fada0380-6856-11eb-87cb-212807ecaba7.png)