from decouple import config
from modulos.funciones import *

url_API="http://api.bcra.gob.ar/estadisticas/v2.0/PrincipalesVariables"

def main():
    try:
        data=extraccion_API(url=url_API)
        grabar_datos(host=config('host'),
                    port=config('port'),
                    dbname=config('dbname'),
                    user=config('user'),
                    password=config('password'),
                    schema=config('schema'),
                    tabla=config('tabla'),
                    df=data)
    except Exception as e :
        print(f'Error {e}')


if __name__=='__main__':
    main()