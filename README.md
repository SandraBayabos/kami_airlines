# KAMI Airlines

## Requirements:

- Python3
- Pip3
- Python environment (e.g. `conda`, `venv`, `pyenv` etc.)
- Postgresql

Follow these steps to get your environment set up:

### 1. Clone the repository:

```
git clone https://github.com/your-username/your-project-name.git
cd kami_airlines
```

### 2. Set up a virtual environment (the following example uses `conda`)

```
conda create --name kami_airlines
conda activate kami_airlines
```

### 3. Install the packages as per the requirements.txt file

```
pip3 install -r requirements.txt
```

### 4. Create the database

- There is a custom function in create_db.py and you may run the following commands to set up the db locally and migrate the necessary airlines table

```
python3 manage.py create_db
python3 manage.py makemigrations kami_workforce_airlines_app
python3 manage.py migrate

```

### 5. To run the server

```
python3 manage.py runserver
```

### 6. REST APIs available

REST APIs can be tested using Postman or curl commands as follows:

#### Example Data for Postman:

```
- Get All Airplanes
GET http://localhost:8000/airlines/api/airplanes/

- Get One Airplane
GET http://localhost:8000/airlines/api/airplanes/2/

- Bulk Create Airplanes
POST http://localhost:8000/airlines/api/airplanes/

Request Body:

[
    {"airplane_id": 1, "passenger_count": 100},
    {"airplane_id": 2, "passenger_count": 200},
    {"airplane_id": 3, "passenger_count": 150},
    {"airplane_id": 4, "passenger_count": 120},
    {"airplane_id": 5, "passenger_count": 180},
    {"airplane_id": 6, "passenger_count": 160},
    {"airplane_id": 7, "passenger_count": 140},
    {"airplane_id": 8, "passenger_count": 110},
    {"airplane_id": 9, "passenger_count": 130},
    {"airplane_id": 10, "passenger_count": 170}
]

- Example Response Body:

[
    {
        "airplane_id": 1,
        "passenger_count": 100,
        "fuel_consumption_per_minute": 0.01,
        "max_flight_time": 20000.0
    },
    {
        "airplane_id": 2,
        "passenger_count": 200,
        "fuel_consumption_per_minute": 0.87,
        "max_flight_time": 459.77
    },
    {
        "airplane_id": 3,
        "passenger_count": 150,
        "fuel_consumption_per_minute": 1.18,
        "max_flight_time": 508.47
    },
    {
        "airplane_id": 4,
        "passenger_count": 120,
        "fuel_consumption_per_minute": 1.4,
        "max_flight_time": 571.43
    },
    {
        "airplane_id": 5,
        "passenger_count": 180,
        "fuel_consumption_per_minute": 1.75,
        "max_flight_time": 571.43
    },
    {
        "airplane_id": 6,
        "passenger_count": 160,
        "fuel_consumption_per_minute": 1.89,
        "max_flight_time": 634.92
    },
    {
        "airplane_id": 7,
        "passenger_count": 140,
        "fuel_consumption_per_minute": 2.0,
        "max_flight_time": 700.0
    },
    {
        "airplane_id": 8,
        "passenger_count": 110,
        "fuel_consumption_per_minute": 2.08,
        "max_flight_time": 769.23
    },
    {
        "airplane_id": 9,
        "passenger_count": 130,
        "fuel_consumption_per_minute": 2.23,
        "max_flight_time": 807.17
    },
    {
        "airplane_id": 10,
        "passenger_count": 170,
        "fuel_consumption_per_minute": 2.42,
        "max_flight_time": 826.45
    }
]

- Update an Airplane's passenger_count
PATCH http://localhost:8000/airlines/api/airplanes/2/

Request Body:

{
    "passenger_count":90
}

- Delete an Airplane
DELETE http://localhost:8000/airlines/api/airplanes/2/

```

#### Example Curl Commands in Terminal

#### Get All Airplanes

- `GET /airlines/api/airplanes/`
- Example Request: `curl http://localhost:8000/airlines/api/airplanes/`

#### Get One Airplane

- `GET /airlines/api/airplanes/{airplane_id}/`
- Example Request: `http://localhost:8000/airlines/api/airplanes/2/`

#### Create New Airplanes (Bulk Create since assignment requires bulk input of up to 10 airplanes)

- `POST /airlines/api/airplanes/`
- Example Request:

```
curl -X POST http://localhost:8000/airlines/api/airplanes/ \
     -H 'Content-Type: application/json' \
     -d '[{"airplane_id": 3, "passenger_count": 150}, {"airplane_id": 4, "passenger_count": 200}]'
```

#### Update an Airplane (assuming only passenger_count will be updated)

- `PATCH /airlines/api/airplanes/{airplane_id}/`
- Example Request:

```
curl -X PATCH http://localhost:8000/airlines/api/airplanes/3/ \
     -H 'Content-Type: application/json' \
     -d '{"passenger_count": 180}'
```

#### Delete an Airplane

- `DELETE /airlines/api/airplanes/{airplane_id}`
- Exmaple Request: `curl -X DELETE http://localhost:8000/airlines/api/airplanes/2/`

### 7. Tests

Testing has been implemented using `django tests` and can be run with the commaned `python3 manage.py test`

The latest Coverage Report is as follows:

```
Name                                                                        Stmts   Miss  Cover
-----------------------------------------------------------------------------------------------
kami_airlines/__init__.py                                                       0      0   100%
kami_airlines/asgi.py                                                           4      4     0%
kami_airlines/settings.py                                                      18      0   100%
kami_airlines/urls.py                                                           3      0   100%
kami_airlines/wsgi.py                                                           4      4     0%
kami_workforce_airlines_app/__init__.py                                         0      0   100%
kami_workforce_airlines_app/admin.py                                            1      0   100%
kami_workforce_airlines_app/apps.py                                             4      0   100%
kami_workforce_airlines_app/migrations/0001_initial.py                          5      0   100%
kami_workforce_airlines_app/migrations/0002_alter_airplane_airplane_id.py       4      0   100%
kami_workforce_airlines_app/migrations/__init__.py                              0      0   100%
kami_workforce_airlines_app/models.py                                          34      6    82%
kami_workforce_airlines_app/serializers.py                                     31      3    90%
kami_workforce_airlines_app/tests.py                                           83      0   100%
kami_workforce_airlines_app/urls.py                                             4      0   100%
kami_workforce_airlines_app/views.py                                           52     14    73%
manage.py                                                                      12      2    83%
-----------------------------------------------------------------------------------------------
TOTAL                                                                         259     33    87%
```
