import pyodbc 


def Database_Connect(server:str, database:str, username:str, password:str):

    args = '''
        DRIVER=ODBC Driver 18 for SQL Server; SERVER= {}; 
        DATABASE= {};UID= {};PWD={};
        '''.format(server,database,username, password)

    conn = pyodbc.connect(args)
    cursor = conn.cursor()
    
    return cursor

def Query_Call(cursor):

    select_query = """here we put the select query"""
    query = cursor.execute(select_query)
    cursor.commit()

    return query
  
