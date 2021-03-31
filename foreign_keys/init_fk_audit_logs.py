import pyodbc

################################## AUDIT_LOGS #################################################


def init_audit_logs_fk(conn, cur):
    try:
        cur.execute("""ALTER TABLE AUDIT_LOGS ADD USERS_ID bigint FOREIGN KEY 
        REFERENCES USERS(USER_ID) """)
        conn.commit()
        print("FK AUDIT_LOGS USERS_ID set")
    except pyodbc.ProgrammingError as e:
        print("  FK AUDIT_LOGS USERS_ID already set")
    try:
        cur.execute("""ALTER TABLE AUDIT_LOGS ADD FDID bigint FOREIGN KEY 
        REFERENCES FDID(FDID) """)
        conn.commit()
        print("FK AUDIT_LOGS FDID set")
    except pyodbc.ProgrammingError as e:
        print("  FK AUDIT_LOGS FDID already set")
    return


def init_all(conn, cur):
    init_audit_logs_fk(conn, cur)
    return
