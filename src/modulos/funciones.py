import requests
import pandas as pd
import warnings
from sqlalchemy import create_engine
import psycopg2
warnings.simplefilter('ignore')


def extraccion_API(url):
    idvar=[1,4,6,7,8,14,19,23,26,30,31,32,40]
    try:
        response=requests.get(url, verify=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("La conexion falló", e)
        return
    
    if response.status_code==200:
        data=response.json()
        df=pd.json_normalize(data,record_path="results")
        print(df.head(2))
        df['valor']=round(df['valor'])
        df['fecha']=pd.to_datetime(df['fecha'])
        df=df[df['idVariable'].isin(idvar)]
        print('df filtrado con exito')
        return df
    else:
        print(f"Error {response.status_code}")
        return 
        
def grabar_datos(df,host,port, dbname,user,password,schema,tabla):
    conn=create_engine(f"postgresql://{user}:{password}@{host}:{port}/{dbname}")
    df.to_sql(tabla, conn,schema=schema, index=False, if_exists='append')
    print("Datos grabados con exito")