import notas.nota as model

class Acciones:

    def crear(self, user):
        print(f'{user[1]} crea una nota')

        titulo = input('Titulo de la nota: ')
        descripcion = input('Descripcion: ')

        nota = model.Nota(user[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f'\nNota guardada: {nota.titulo}')
        else:
            print('No se guardó la nota')

    def mostrar(self, user):
        try:
            print(f'Ok, {user[1]}! Estas son las notas que creaste hasta el momento')
            nota = model.Nota(user[0])
            notas = nota.listar()
            for nota in notas:
                print('\n**************************')
                print(nota[2])
                print(nota[3])
        except Exception as err:
            print(type(err))

    def borrar(self, usuario):
        print(f'\n Oka {usuario[1]}!! Vamos a borrar notas')

        titulo = input('Nombre de la nota a borrar')

        nota = model.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f'Borramos la nora: {nota.titulo}')

        else:
            print('no se ha eliminado la nora, gil')