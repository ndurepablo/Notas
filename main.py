"""
Proyect:
    - Abrir asitente
    - Login o Resgistro
    - Registro: crear un suario en la db
    - Login: identificar al usuario
    - Crear, mostrar, borrar nota
"""
from usuarios import acciones

doit = acciones.Acciones()

print('Registro o Login')
accion = input('Hola, elejí una opcion: ')
if accion == 'Registro':
    doit.signup()

elif accion == 'Login':
    doit.login()