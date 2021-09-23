import os
import pandas as pd
# import sqlite3 as mysql
# from sqlite3 import Error
import pymysql as mysql
from pymysql import Error

def connect_to_db(dbName=None):

    conn = mysql.connect(user='root', password='root',
                             host='localhost', database = dbName)
    cur = conn.cursor()
    return conn, cur

def create_db(dbName: str) -> None:

    conn, cur = connect_to_db()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
    conn.commit()
    cur.close()

def create_table(dbName: str) -> None:

    conn, cur = connect_to_db(dbName)
    sqlFile = 'schema.sql'
    fd = open(sqlFile, 'r')
    readSqlFile = fd.read()
    fd.close()

    sqlCommands = readSqlFile.split(';')

    for command in sqlCommands:
        try:
            res = cur.execute(command)
        except Exception as ex:
            print("Command skipped: ", command)
            print(ex)
    conn.commit()
    cur.close()
    return

def insert_to_table(dbName: str, df: pd.DataFrame, table_name: str) -> None:

    conn, cur = connect_to_db(dbName)

    for _, row in df.iterrows():
        sqlQuery = f"""INSERT INTO {table_name} (timeperiod,  flow1,  occupancy1,  speed1,  flow2,  occupancy2,  speed2, flow3, occupancy3, speed3, flow4, occupancy4, speed4, flow5, occupancy5, speed5, flow6, occupancy6, speed6, flow7, occupancy7, speed7, flow8, occupancy8, speed8)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        data = [row[i] for i in range(len(row))]
        print(data)
        try:
            # Execute the SQL command
            cur.execute(sqlQuery, data)
            # Commit your changes in the database
            conn.commit()
            #print("Data Inserted Successfully")
        except Exception as e:
            conn.rollback()
            print("Error: ", e)
    return

if __name__ == "__main__":
    create_db(dbName='10acad_sensor_data')
    connect_to_db(dbName='10acad_sensor_data')
    create_table(dbName='10acad_sensor_data')
    for filename in os.listdir('../pems_sorted/station=402260/'):
        df = pd.read_parquet('../pems_sorted/station=402260/'+filename, engine='pyarrow').head(1)
        print(df)
        df = df.fillna(value='NULL')
        insert_to_table(dbName='10acad_sensor_data', df=df, table_name='sensor_data')
