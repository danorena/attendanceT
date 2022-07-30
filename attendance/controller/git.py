# Creamos una funcion para hacer git push
def push():
    # importamos la libreria para abrir el cmd
    from os import system
    # Importamos la libreria para hacer numeros random
    import random
    # Generamos un numero random
    rand = random.randint(0,9999999) + random.randint(0,9999999)
    # Hacemos un try para saber que no nos tire ningun error
    # Hacemos un push con el debido proceso
    try:
        system('git add .')
        system(f"git commit -m '{rand}'")
        system('git push')
        print('Hecho')
    except:
        print('Hubo un error haciendo el commit')
    # return 'No le pare bolas'

# print(push())