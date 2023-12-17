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

```
python3 manage.py create_db
python3 manage.py makemigrations kami_workforce_airlines_app
python3 manage.py migrate

```

### 5. To run the server

```
python3 manage.py runserver
```
