# IOT_API

Example_url : https://xxiot.herokuapp.com

## Main Function

### Index

hello world!
- GET https://xxiot.herokuapp.com

### Temperature API

List Operation
- GET https://xxiot.herokuapp.com/api/temps
- POST ADD(VALUE,PLACE) => https://xxiot.herokuapp.com/api/temps

Single Operation
- GET https://xxiot.herokuapp.com/api/temps/<id>
- PUT UPDATE(VALUE,PLACE) => https://xxiot.herokuapp.com/api/temps/<id>
- DELETE  https://xxiot.herokuapp.com/api/temps/<id>

**Structure**

- id(Int)
- value(String)
- place(String)
- creation_date(DateTime)
  
## Test

### HTTP Test
- python api_http_test.py
- select correct service

### Basic API Test
- python api_basic_test.py
- select correct service

### Curl

- curl  -i -H "Content-Type: application/json" -X POST -d '{"place":"pxl","value":"20"}' https://xxiot.herokuapp.com/api/temps
- curl  -i -H "Content-Type: application/json" -X GET  https://xxiot.herokuapp.com/api/temps

## Requirements

### Packages

- Flask
- Flask-Restful
- Flask-Sqlalchemy
- Flask-WTF
- Flask-Bootstrap
- Flask-Migrate
- Psycopg2-binary
- Gunicorn
- requests

### Runtime Version

- python=3.6.6

## Deploy 

- uwsgi 
- systemd
- docker


[How to deploy](deploy/README.MD)