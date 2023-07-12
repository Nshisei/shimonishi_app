import psycopg2
name='Bushi' 
# データベースに接続
connection = psycopg2.connect(host='localhost',
                             user='postgres',
                             database='db_clothes')
with connection:
    with connection.cursor() as cursor:
        # データ読み込み
        sql = "SELECT id FROM namelist where name = %s"
        cursor.execute(sql,(name,))
        id = cursor.fetchall()
        id=id[0]
        print(id)
        sql="SELECT * FROM clothelist where person_id = %s"
        cursor.execute(sql,(id,))
        result=cursor.fetchall()
        print(result)
