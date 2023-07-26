import psycopg2
import pandas as pd
# データベースに接続
db_config = {
	'host': 'localhost',
	'port': '5432',
	'user': 'postgres',
	'database': 'db_clothes'}

def load_query_to_dataframe(sql):
    with psycopg2.connect(**db_config) as conn:
        df = pd.read_sql(sql,conn)
        return df


def exec_sql_cmd(sql):
    with psycopg2.connect(**db_config) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)

def get_info_from_db(name):
    with open('/home/suita/shimonishi_app/post_database/sql/get_clothes.sql') as f:
        sql = f.read()
    sql = sql.replace('<NAME>', name)
    result = load_query_to_dataframe(sql).to_numpy().tolist()
    return result

def get_gender(name):
    with open('/home/suita/shimonishi_app/post_database/sql/get_users.sql') as f:
        sql = f.read()
    sql = sql.replace('<NAME>', name)
    result = load_query_to_dataframe(sql)['gender'].iloc[0]
    return result

def get_all_data():
    with open('/home/suita/shimonishi_app/post_database/sql/get_all_data.sql') as f:
            sql = f.read()
    result = load_query_to_dataframe(sql).to_string()
    return result

def insert_clothes(person_id, color, shape, season):
    try:
        id = get_all_data().count('\n') + 1
        print(id, person_id, color, shape, season)
        sql = f"insert into clothelist1 values ({id}, {person_id}, '{color}','{shape}', '{season}');"
        exec_sql_cmd(sql)
        return
    except Exception as e:
        return e

def delete_clothes(id):
    try:
        sql = f"delete from clothelist1 where id = {id};"
        exec_sql_cmd(sql)
        return
    except Exception as e:
        return e

def insert_user(id, name, gender):
    # try:
    sql = f"insert into namelist1 values ({id}, '{name}', '{gender}');"
    exec_sql_cmd(sql)
    return
    # except Exception as e:
    #     return e

def delete_user(id):
    try:
        sql = f"delete from namelist1 where id = {id};"
        exec_sql_cmd(sql)
        return
    except Exception as e:
        return e

if __name__ == '__main__':
    # insert_user(0, 'test','w')
    # print(get_all_data())
    delete_user(0)
    print(get_all_data())
    # delete_clothes('12')
    # delete_clothes('14')
    # insert_clothes('23026','白','シャツ','夏')
    # print(get_all_data())
    # print(get_gender('Bushi'))
    # print(get_all_data())
