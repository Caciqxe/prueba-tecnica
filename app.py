import subprocess

path = './scripts/'
scripts = [
    'eliminar_tablas.py',
    'revisar_tablas.py',
    'modelo_datos.py',
    'carga_datos.py',
    'revisar_tablas.py',
    'query.py'
]

for script in scripts:
    print(f'ejecutando {script}...')
    subprocess.run(["python", path+script])
    print(f'se ejecuto correctamente {script}!')