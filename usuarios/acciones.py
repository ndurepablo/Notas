from usuarios import usuarios as model
import notas.acciones

class Acciones:
    def signup(self):
        print('\nOk, vamos a registrarnos')
        nombre = input('Tu nombre es:')
        apellido = input('Apellido: ')
        email = input('Email: ')
        password = input('Contraseña: ')

        user = model.User(nombre, apellido, email, password)
        signup = user.signup()

        if signup[0] >= 1:
            print(f"{signup[1].nombre} se ha registrado correctamente con el mail {signup[1].email}")
        else:
            print('Registro fallido')

    def login(self):
        print('Identificate, por favor')

        try: 
            email = input('Email: ')
            password = input('Contraseña: ')

            usuario = model.User('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f'Login correcto, bienvenido {login[1]}. Te registraste el {login[5]}')
                self.nexstep(login)
        except Exception as err:
            print(type(err))
            print(type(err).__name__) 
            print('hubo un error')

    def nexstep(self, user):
        print("""
            - Crear
            - Mostrar 
            - Eliminar 
            - Salir
        """)
        action = input('Que querés hacer con tus notas?: ')
        doit = notas.acciones.Acciones()

        if action == 'Crear':
            doit.crear(user)
            self.nexstep(user)

        elif action == 'Mostrar':
            doit.mostrar(user)
            self.nexstep(user)

        elif action == 'Eliminar':
            doit.borrar(user)
            self.nexstep(user)

        elif action == 'Salir':
            exit()