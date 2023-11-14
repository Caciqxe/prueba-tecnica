import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:1234@db:5432/example')

users_col = [
    'user_id',
    'name_user',
    'rut_user',
]

vehicles_col = [
    'vehicle_id'
]

trips_col = [
    'trip_id',
    'user_id',
    'vehicle_id',
    'membership_id',
    'booking_time',
    'status_id',
    'start_time',
    'end_time',
    'start_lat',
    'start_lon',
    'end_lat',
    'end_lon',
    'travel_dist',
    'price_amount',
    'price_tax',
    'price_total'
]

df = pd.read_csv('./files/trips.csv')
df['booking_time'] = pd.to_datetime(df['booking_time'])

df_users = df[users_col].drop_duplicates()
df_vehicles = df[vehicles_col].drop_duplicates()

df_fact = df[trips_col]

df_users.to_sql('users', con=engine, index=False, if_exists='append')
df_vehicles.to_sql('vehicles', con=engine, index=False, if_exists='append')
df_fact.to_sql('trips', con=engine, index=False, if_exists='append')


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