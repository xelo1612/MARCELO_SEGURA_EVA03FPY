
import json 
menup =['Ver Listado de Pinturas',
        'Buscar Pintura',
        'Agregar Pintura',
        'Eliminar Pintura',
        'Exportar Pinturas']


lista = ['PINTURA:','CODIGO:' ]
while True:
    print('bienvenido a la gestion de inventario de Pinturas Acrílicas Mandarina.\n')
    print('¿que desea hacer?')
    for i,opt in enumerate(menup):
        print(f'{i+1}. {opt}')
    input('\n')
    while True:
        ans = (menup)
        if ans =='1':
            exportar(ruta_j)
        elif ans =='2':
            pass
        elif ans == '3':
            pass
        elif ans == '4':
            pass
        elif ans == '5':
            pass
        else:
            print('Opcion no valida!')
        break