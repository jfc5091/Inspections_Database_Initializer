import pyodbc

################################## FDID #################################################


def init_fdid_table(conn, cur):
    if cur.tables(table='FDID', tableType='TABLE').fetchone():
        # if you add columns other than basic add here and add below
        print("  FDID exists")
    else:
        cur.execute("""CREATE TABLE FDID (
           FDID bigint NOT NULL IDENTITY(1,1) PRIMARY KEY,
           DEPARTMENT varchar(255),
           CITY varchar(255),
           STATE varchar(255),
           )""")
        print("FDID created")
    conn.commit()
    return


def init_all(conn, cur):
    init_fdid_table(conn, cur)
    return
