# from tugaspwl4 import db_connect
import pymysql

def init_db():
    conn = pymysql.connect(host='localhost', user='root', password='', db='pyramidtest')
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        year INT NOT NULL
    );
    """)
    
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    init_db()