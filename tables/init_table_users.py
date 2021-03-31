import pyodbc

################################## USERS #################################################


def init_users_table(conn, cur):
    if cur.tables(table='USERS', tableType='TABLE').fetchone():
        # if you add columns other than basic add here and add below
        print("  USERS exists")
    else:
        cur.execute("""CREATE TABLE USERS (
           USER_ID bigint NOT NULL IDENTITY(1,1) PRIMARY KEY,
           USERNAME nvarchar(MAX) NOT NULL,
           PASSWORD ntext NOT NULL,
           EMAIL ntext,
           ENABLED bit
           )""")
        print("USERS created")
    conn.commit()
    return

def init_users_authorities_table(conn, cur):
    if cur.tables(table='USERS_AUTHORITIES', tableType='TABLE').fetchone():
        # if you add columns other than basic add here and add below
        print("  USERS_AUTHORITIES exists")
    else:
        cur.execute("""CREATE TABLE USERS_AUTHORITIES (
           AUTHORITY_ID bigint NOT NULL IDENTITY(1,1) PRIMARY KEY,
           INSPECTION_AUTHORITY ntext, 
           LOGIN_AUTHORITY ntext
           )""")
        print("USERS_AUTHORITIES created")
    conn.commit()
    return


def init_all(conn, cur):
    init_users_table(conn, cur)
    init_users_authorities_table(conn, cur)
    return
