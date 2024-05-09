import mysql.connector


def save_data(table,my_list):
    cnx = mysql.connector.connect(user='root',
                              password='admin',
                              host='localhost',
                              database='student')
    table=table
    insertion_data=tuple(my_list)
    query = (f"describe {table}")
    cursor = cnx.cursor()
    cursor.execute(query)
    column_info=cursor.fetchall()
    column_names =tuple([col_info[0] for col_info in column_info if not col_info[5]])
    num_placeholders = len(column_names) * "%s,"
    insert_query = f"INSERT INTO {table} ({', '.join(column_names)}) VALUES ({num_placeholders[:-1]})" 
    print(insert_query)
    cursor.execute(insert_query,insertion_data)
    cnx.commit()

    
    
  
    #create connection

#save_data("student",["Jeevan","kondaveeti","20/12/1997","abc",9492]) 