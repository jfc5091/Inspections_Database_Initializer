import pyodbc

################################## INSPECTIONS #################################################


def init_inspection_fk(conn, cur):
    try:
        cur.execute("""ALTER TABLE INSPECTION ADD INSPECTOR_ID bigint FOREIGN KEY 
        REFERENCES INSPECTOR(INSPECTOR_ID) """)
        conn.commit()
        print("FK INSPECTION INSPECTOR_ID set")
    except pyodbc.ProgrammingError as e:
        print("  FK INSPECTION INSPECTOR_ID already set")
    try:
        cur.execute("""ALTER TABLE INSPECTION ADD PROPERTY_ID bigint FOREIGN KEY 
        REFERENCES PROPERTY(PROPERTY_ID) """)
        conn.commit()
        print("FK INSPECTION PROPERTY_ID set")
    except pyodbc.ProgrammingError as e:
        print("  FK INSPECTION PROPERTY_ID already set")
    try:
        cur.execute("""ALTER TABLE INSPECTION ADD INSPECTION_CHECKLIST_ID bigint FOREIGN KEY 
        REFERENCES INSPECTION_CHECKLIST(INSPECTION_CHECKLIST_ID) """)
        conn.commit()
        print("FK INSPECTION INSPECTION_CHECKLIST_ID set")
    except pyodbc.ProgrammingError as e:
        print("  FK INSPECTION INSPECTION_CHECKLIST_ID already set")
    try:
        cur.execute("""ALTER TABLE INSPECTION ADD FDID bigint FOREIGN KEY 
        REFERENCES FDID(FDID) """)
        conn.commit()
        print("FK INSPECTION FDID set")
    except pyodbc.ProgrammingError as e:
        print("  FK INSPECTION FDID already set")
    return


def init_inspector_fk(conn, cur):
    try:
        cur.execute("""ALTER TABLE INSPECTOR ADD USER_ID bigint FOREIGN KEY 
        REFERENCES USERS(USER_ID) """)
        conn.commit()
        print("FK INSPECTOR USER_ID set")
    except pyodbc.ProgrammingError as e:
        print("  FK INSPECTOR USER_ID already set")
    try:
        cur.execute("""ALTER TABLE INSPECTOR ADD FDID bigint FOREIGN KEY 
        REFERENCES FDID(FDID) """)
        conn.commit()
        print("FK INSPECTOR FDID set")
    except pyodbc.ProgrammingError as e:
        print("  FK INSPECTOR FDID already set")
    return


def init_inspection_action_fk(conn, cur):
    try:
        cur.execute("""ALTER TABLE INSPECTION_ACTION ADD INSPECTION_ID bigint FOREIGN KEY 
        REFERENCES INSPECTION(INSPECTION_ID) """)
        conn.commit()
        print("FK INSPECTION_ACTION INSPECTION_ID set")
    except pyodbc.ProgrammingError as e:
        print("  FK INSPECTION_ACTION INSPECTION_ID already set")
    try:
        cur.execute("""ALTER TABLE INSPECTION_ACTION ADD FDID bigint FOREIGN KEY 
        REFERENCES FDID(FDID) """)
        conn.commit()
        print("FK INSPECTION_ACTION FDID set")
    except pyodbc.ProgrammingError as e:
        print("  FK INSPECTION_ACTION FDID already set")
    return


def init_all(conn, cur):
    init_inspection_fk(conn, cur)
    init_inspector_fk(conn, cur)
    init_inspection_action_fk(conn, cur)
    return
