import pyodbc

################################## USERS #################################################


def init_users_fk(conn, cur):
    try:
        cur.execute("""ALTER TABLE USERS ADD USERS_AUTHORITIES_ID bigint FOREIGN KEY 
        REFERENCES USERS_AUTHORITIES(AUTHORITY_ID) """)
        conn.commit()
        print("FK USERS USERS_AUTHORITIES_ID set")
    except pyodbc.ProgrammingError as e:
        print("  FK USERS USERS_AUTHORITIES_ID already set")
    try:
        cur.execute("""ALTER TABLE USERS ADD FDID bigint FOREIGN KEY 
        REFERENCES FDID(FDID) """)
        conn.commit()
        print("FK USERS FDID set")
    except pyodbc.ProgrammingError as e:
        print("  FK USERS FDID already set")
    return


def init_all(conn, cur):
    init_users_fk(conn, cur)
    return
