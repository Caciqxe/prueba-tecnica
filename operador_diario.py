import pandas as pd
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner': 'sebastian cartes',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 11),
    'email_on_failure': 'sebastian.cartes.s@gmail.com',
    'email_on_retry': 'sebastian.cartes.s@gmail.com',
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'cargar_df_a_sql',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
)

def cargar_df_a_sql():
    engine = create_engine('postgresql://postgres:1234@db:5432/example')

    hoy = datetime.now().strftime('%Y-%m-%d').date()
    
    df = pd.read_csv('./files/trips.csv')
    
    df['booking_time'] = pd.to_datetime(df['booking_time']).dt.date
    df = df[df['booking_time'] == hoy]

    resumen_diario = df.groupby(df['booking_time'].dt.date).agg(
    conteo_usuarios=('user_id', 'count'),
    precio_total=('price_total','sum'),
    precio_promedio=('price_total','mean'),
    metros_total=('travel_dist','sum')
    ).reset_index()

    resumen_diario = resumen_diario.rename(columns={'booking_time': 'dia'})
    resumen_diario.index.name = 'resumen_id'
    resumen_diario = resumen_diario.reset_index()

    resumen_diario.to_sql('resumen_diario', con=engine, index=False, if_exists='append')

cargar_df_a_sql_task = PythonOperator(
    task_id='cargar_resumen_diario',
    python_callable=cargar_df_a_sql,
    dag=dag,
)