from datetime import datetime, timedelta, timezone

from airflow.sdk import DAG, dag, task
from airflow.providers.standard.operators.empty import EmptyOperator

# Often, many Operators inside a Dag need the same set of default arguments (such as their retries). 
# Rather than having to specify this individually for every Operator, 
# you can instead pass default_args to the Dag when you create it, 
# and it will auto-apply them to any operator tied to it:
default_args = {
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# you can use a context manager, which will add the DAG to anything inside it implicitly:
with DAG(
    "First_ensf612_dag", start_date=datetime(2021, 1, 1, tzinfo=timezone.utc),
    schedule=timedelta(days=1), catchup=False, tags=["example"], 
    description="A simple tutorial DAG",
    default_args=default_args,
) as context_dag:
    op = EmptyOperator(task_id="task_1")


# Or, you can use a standard constructor, passing the dag into any operators you use:
my_dag = DAG("Second_ensf612_dag", start_date=datetime(2021, 1, 1, tzinfo=timezone.utc),
             schedule="@daily", catchup=False)

op = EmptyOperator(task_id="task_2", dag=my_dag)


# Or, you can use the @dag decorator to turn a function into a DAG generator:
@dag(start_date=datetime(2021, 1, 1, tzinfo=timezone.utc), 
     schedule="@daily", catchup=False, tags=["decorator"])
def generate_dag():
    op = EmptyOperator(task_id="task_3")

dag_decorator = generate_dag()

