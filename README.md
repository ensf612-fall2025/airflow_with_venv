## Steps to install Apache Airflow
1. Create your virtual environment to isolate dependencies:
- `python3.12 -m venv airflow_venv` - on Linux and MacOS
- `py -3.12 -m venv airflow_venv` - on Windows (or Use WSL with Linux command above)

2. Activate the virtual environment:
- `source airflow_venv/bin/activate` - on Linux and MacOS
- `.\airflow_venv\Scripts\activate` - on Windows (or Use WSL with Linux command)

3. Set the airflow project directory (your desired folder location):
- `export AIRFLOW_HOME=~/big_data/airflow_with_venv` - on Linux/MacOS
- `set AIRFLOW_HOME=~/big_data/airflow_with_venv` - on Windows (or Use WSL with Linux command above)

4. Set Python and Airflow versions:
- `export AIRFLOW_VERSION=3.1.2` - on Linux/MacOS
- `export PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"` - on Linux/MacOS
- `export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"` - on Linux/MacOS
- confirm by running the command `echo ${CONSTRAINT_URL}` and you should see the output url`"https://raw.githubusercontent.com/apache/airflow/constraints-3.1.2/constraints-3.12.txt"` in you terminal
- on Windows, use `set` as before.

5. Install using `pip`:
- `pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"`

6. Check for version:
- `airflow version`

6. Initialize airflow:
- `airflow standalone` - this command initializes the database, creates a user, and starts all components.

7. Navigate to `http://localhost:8080/`

7. To log in, the default admin username and password can be found in the file: `~/big_data/airflow_with_venv/simple_auth_manager_passwords.json.generated`.
to access it, you can run `cat ~/big_data/airflow_with_venv/simple_auth_manager_passwords.json.generated` to print to the console.
Alternatively, go to the folder: `code ~/big_data/airflow_with_venv`.


## Additional Information
- Hide Example Dags to declutter UI: 
    - in your terminal: `export AIRFLOW__CORE__LOAD_EXAMPLES=False`
    - then run: `airflow db reset`
    - then `airflow standalone`

- Show/hide Configs from UI: `export AIRFLOW__API__EXPOSE_CONFIG=True`
