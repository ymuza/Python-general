import psycopg2

conexion1 = psycopg2.connect(database="python-test", user="postgres", host="localhost", password=32874993)
cursor1 = conexion1.cursor()
sql = "insert into personas(nombre, apellido, edad) values (%s,%s,%s)"
datos = ("carlos", "lopez", 23)
cursor1.execute(sql, datos)
datos = ("lucas", "martinez", 37)
cursor1.execute(sql, datos)
datos = ("giancarlo", "exposito", 45)
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close()
