import json

def agregar(jfile):
    if not jfile.exists():
        jfile.touch()
        print('el archivo se ha creado')
def exportar(ruta_j):
    if not ruta_j.stat().st_statz == 0:
        print('no hay datos guardados')