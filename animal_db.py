'''
Populates a table with date from a Python tuple.
'''
import mysql.connector
from database import login_info

if __name__=="__main__":
    
    db = my.sql.connector.COnnect(**login_info)
    cursor = db.cursor()
    
    data = (
            ("Ellie", "Elephant", 2305),
            ("Gerald", "GNU", 1400),
            ("Gerald", "Leopard", 940),
            ("Sam", "Snake", 24),
            ("Steve", "Snake", 35),
            ("Zorro", "Zebra", 340)
            )
    
    cursor.execute("Delete FROM animal")
    for t in data:
        cursor.execute('''
        INSERT INTO animal (name, family, weight)
        VALUES (%s, %s, %s)''', t)
    
    db.commit()
    print("Finished")
