import sqlite3
import datetime

# Works to do ---
# 1st verifying then creating database

# today = str(datetime.date.today())
# classroom_id = today.replace("-","_")
# conn = sqlite3.connect("databases/PDFS.db")
# cursor = conn.cursor()
# cursor.execute("CREATE TABLE TEST(pdf,extracted)")
# cursor.execute("""INSERT OR IGNORE INTO TEST1 (pdf, extracted) VALUES
#                ('B.pdf','False')""")
# conn.commit()
# cursor.execute("CREATE TABLE IF NOT EXITS TEST")
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS TEST1(
#     pdf TEXT UNIQUE,
#     extracted INTEGER
# )
# """)

# res = cursor.execute("SELECT * FROM TEST1")
# print(cursor.fetchall())




class DatabaseConn:
    def __init__(self,db_name:str):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connect()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        
        self.close()
        
    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            # self.connection.row_factory = sqlite3.Row  
            return True
        except Exception as e:
            raise sqlite3.DatabaseError(f"Connection failed: {str(e)}")
    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def table_exists(self, table_name:str):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        return cursor.fetchone() is not None
    
    def create_table(self,table_name):  
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name}(
                pdf TEXT UNIQUE,
                handwritten INTEGER,
                extracted INTEGER
            )
            """)
            return True
        except Exception as e:
            raise Exception(e)

    def insert_value(self,table_name:str,pdf:str,handwritten:int,extracted:int)->bool:
        cursor = self.connection.cursor()
        try:    
            cursor.execute(f"""INSERT OR IGNORE INTO {table_name} (pdf,handwritten, extracted) VALUES
            ('{pdf}','{handwritten}','{extracted}')""")
            self.connection.commit()
            return True
        except Exception as e:
            raise Exception(e)  
    
    def print_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master")
        print(cursor.fetchall())
    
    def show_table_data(self,table_name):
        cursor = self.connection.cursor()            
        cursor.execute(f"SELECT * FROM {table_name}")
        print(cursor.fetchall())
    
    def delete_table(self,table_name):
        cursor = self.connection.cursor()
        cursor.execute(f"DROP TABLE {table_name}")

    def update_extracted(self,table_name,pdf,extracted=1):
        cursor = self.connection.cursor()
        update_query = f"""
        UPDATE {table_name}
        SET extracted = {extracted}  
        WHERE pdf = '{pdf}'
        """
        try:
            cursor.execute(update_query)
            self.connection.commit()
            return True
        except Exception as e:
            raise Exception(e)




# database = DatabaseConn("databases/PDFS.db")
# print(database.connect())
# print(database.create_table('OOPSTEST'))
# print(database.insert_value("OOPSTEST","A.pdf",1,1))
# print(database.table_exists('OOPTEST'))
# database.print_tables()

# print(database.update_extracted("OOPSTEST",'A.pdf',0))
# database.show_table_data("OOPSTEST")






# def insert_data(pdfname:str,extracted):
        
#     if table_exists(conn,today):
#         print(True)
#     else:
#         print(False)


# cursor.execute(f"INSERT INTO date_{today} VALUES('C','D');")
# cursor.close()
# cursor.execute(f"SELECT pdf FROM date_{today}")
# print(cursor.fetchall())
# cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='date_{today}'")
# print(cursor.fetchone())

# res = cursor.execute("SELECT name FROM sqlite_master")
# print(res.fetchall())

# cursor.execute(f"DROP DATABASE pdfs.db")
# cursor.execute(f"DROP TABLE date_{today};")
# cursor.execute(f"CREATE TABLE date_{today}(pdf, is_extraced)")