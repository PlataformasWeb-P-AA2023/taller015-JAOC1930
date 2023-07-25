import pandas as pd
import requests

propietarios = pd.read_csv('data/propietarios.csv', delimiter='|')
print(propietarios)

for index, row in propietarios.iterrows():
    cedula = row['cedula']
    nombre = row['nombre']
    apellido = row['apellido']
    
    data = {
        'cedula': cedula,
        'nombre': nombre,
        'apellido': apellido
    }
    
    r = requests.post('http://127.0.0.1:8000/propietarios/', data=data, auth=('jaoc', 'UTPLUTPL'))
    
    if r.status_code == 201:
        print(f"Propietario '{nombre} {apellido}' creado exitosamente.")
    else:
        print(f"Error al crear el propietario '{nombre} {apellido}'. Error {r.status_code}: {r.text}")


edificios = pd.read_csv('data/edificios.csv', delimiter='|')

for index, row in edificios.iterrows():
    nombre = row['nombre']
    direccion = row['dirección']
    ciudad = row['ciudad']
    tipo = row['tipo']

    data = {
        'nombre': nombre,
        'direccion': direccion,
        'ciudad': ciudad,
        'tipo': tipo
    }
    
    r = requests.post('http://127.0.0.1:8000/edificios/', data=data, auth=('jaoc', 'UTPLUTPL'))
    
    if r.status_code == 201:
        print(f"Edificio '{nombre}' creado exitosamente.")
    else:
        print(f"Error al crear el propietario '{nombre} {apellido}'. Error {r.status_code}: {r.text}")