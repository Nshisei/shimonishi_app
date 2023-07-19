import psycopg2
import pandas as pd
# データベースに接続
db_config = {
	'host': 'localhost',
	'port': '5432',
	'user': 'postgres',
	'database': 'db_clothes'}
SQL = """
    SELECT DISTINCT
        shape
        , color
        , season
    FROM
        namelist n
    LEFT JOIN
        clothelist l
    ON
        n.id = l.person_id
    WHERE
        n.name = '<NAME>'
    ;
    """
def load_query_to_dataframe(sql):
	with psycopg2.connect(**db_config) as conn:
		df = pd.read_sql(sql,conn).to_numpy().tolist()
		return df

def get_info_from_db(name):
    sql = SQL.replace('<NAME>', name)
    result = load_query_to_dataframe(sql)
    return result

if __name__ == '__main__':
    name = 'Bushi' 
    print(get_info_from_db(name))