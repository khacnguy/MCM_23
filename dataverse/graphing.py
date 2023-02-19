import sqlite3
import matplotlib.pyplot as plt



def create_connection(db_file):
    """ 
    Description: 
        create a database connection to the SQLite database
    
    Input:
        db_file: database file
    
    Return: 
        Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def main():
    global conn, cur
    conn = create_connection('dataverse/data.sql')
    cur = conn.cursor()

    plt.plot([1,2,3,4])
    plt.ylabel('some numbers')
    plt.show()

main()
