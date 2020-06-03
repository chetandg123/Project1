import psycopg2
try:
    connection = psycopg2.connect(database="cqubedev", user = "cqubedev", password = "tibil123", host ="localhost", port = "5432")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # # Print PostgreSQL version
    # cursor.execute("SELECT version();")
    # record = cursor.fetchone()
    # print("You are connected to - ", record,"\n")

    # list_tables = cursor.fetchall()
    # print(list_tables)
    # for t_name_table in list_tables:
    #     print(t_name_table + "\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")