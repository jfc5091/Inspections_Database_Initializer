import pyodbc

################################## AUDIT_LOGS #################################################


def init_audit_logs_table(conn, cur):
    if cur.tables(table='AUDIT_LOGS', tableType='TABLE').fetchone():
        # if you add columns other than basic add here and add below
        print("  AUDIT_LOGS exists")
    else:
        cur.execute("""CREATE TABLE AUDIT_LOGS (
           AUDIT_LOGS_ID bigint NOT NULL IDENTITY(1,1) PRIMARY KEY,
           REQUEST ntext,
           REQUEST_TYPE ntext,
           REQUEST_URI ntext,
           RESPONSE_STATUS int,
           RESPONSE ntext,
           DATE datetime
           )""")
        print("AUDIT_LOGS created")
    conn.commit()
    return


def init_all(conn, cur):
    init_audit_logs_table(conn, cur)
    return
