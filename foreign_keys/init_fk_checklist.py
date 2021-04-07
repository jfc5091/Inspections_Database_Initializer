import pyodbc

################################## CHECKLISTS #################################################


def init_inspection_checklist_fk(conn, cur):
    try:
        cur.execute("""ALTER TABLE INSPECTION_CHECKLIST ADD FDID bigint FOREIGN KEY 
        REFERENCES FDID(FDID) """)
        conn.commit()
        print("FK INSPECTION_CHECKLIST FDID set")
    except pyodbc.ProgrammingError as e:
        print("  FK INSPECTION_CHECKLIST FDID already set")
    return


def init_inspection_checklist_item_fk(conn, cur):
    try:
        cur.execute("""ALTER TABLE INSPECTION_CHECKLIST_ITEM ADD INSPECTION_CHECKLIST_ID bigint FOREIGN KEY 
        REFERENCES INSPECTION_CHECKLIST(INSPECTION_CHECKLIST_ID) """)
        conn.commit()
        print("FK INSPECTION_CHECKLIST_ITEM INSPECTION_CHECKLIST_ID set")
    except pyodbc.ProgrammingError as e:
        print("  FK INSPECTION_CHECKLIST_ITEM INSPECTION_CHECKLIST_ID already set")
    try:
        cur.execute("""ALTER TABLE INSPECTION_CHECKLIST_ITEM ADD FIRE_CODE_ID bigint FOREIGN KEY 
        REFERENCES FIRE_CODE(FIRE_CODE_ID) """)
        conn.commit()
        print("FK INSPECTION_CHECKLIST_ITEM FIRE_CODE_ID set")
    except pyodbc.ProgrammingError as e:
        print("  FK INSPECTION_CHECKLIST_ITEM FIRE_CODE_ID already set")
    try:
        cur.execute("""ALTER TABLE INSPECTION_CHECKLIST_ITEM ADD FDID bigint FOREIGN KEY 
        REFERENCES FDID(FDID) """)
        conn.commit()
        print("FK INSPECTION_CHECKLIST_ITEM FDID set")
    except pyodbc.ProgrammingError as e:
        print("  FK INSPECTION_CHECKLIST_ITEM FDID already set")
    return


def init_fire_code_fk(conn, cur):
    try:
        cur.execute("""ALTER TABLE FIRE_CODE ADD FDID bigint FOREIGN KEY 
        REFERENCES FDID(FDID) """)
        conn.commit()
        print("FK FIRE_CODE FDID set")
    except pyodbc.ProgrammingError as e:
        print("  FK FIRE_CODE FDID already set")
    return


def init_inspection_violation_fk(conn, cur):
    try:
        cur.execute("""ALTER TABLE INSPECTION_VIOLATION ADD FIRE_CODE_ID bigint FOREIGN KEY 
        REFERENCES FIRE_CODE(FIRE_CODE_ID) """)
        conn.commit()
        print("FK INSPECTION_VIOLATION FIRE_CODE_ID set")
    except pyodbc.ProgrammingError as e:
        print("  FK INSPECTION_VIOLATION FIRE_CODE_ID already set")
    try:
        cur.execute("""ALTER TABLE INSPECTION_VIOLATION ADD INSPECTION_VIOLATION_STATUS_ID bigint FOREIGN KEY 
        REFERENCES INSPECTION_VIOLATION_STATUS(INSPECTION_VIOLATION_STATUS_ID) """)
        conn.commit()
        print("FK INSPECTION_VIOLATION INSPECTION_VIOLATION_STATUS_ID set")
    except pyodbc.ProgrammingError as e:
        print("  FK INSPECTION_VIOLATION INSPECTION_VIOLATION_STATUS_ID already set")
    try:
        cur.execute("""ALTER TABLE INSPECTION_VIOLATION ADD INSPECTION_ID bigint FOREIGN KEY 
        REFERENCES INSPECTION(INSPECTION_ID) """)
        conn.commit()
        print("FK INSPECTION_VIOLATION INSPECTION_ID set")
    except pyodbc.ProgrammingError as e:
        print("  FK INSPECTION_VIOLATION INSPECTION_ID already set")
    try:
        cur.execute("""ALTER TABLE INSPECTION_VIOLATION ADD INSPECTION_CHECKLIST_ITEM_ID bigint FOREIGN KEY 
        REFERENCES INSPECTION_CHECKLIST_ITEM(INSPECTION_CHECKLIST_ITEM_ID) """)
        conn.commit()
        print("FK INSPECTION_VIOLATION INSPECTION_CHECKLIST_ITEM_ID set")
    except pyodbc.ProgrammingError as e:
        print("  FK INSPECTION_VIOLATION INSPECTION_CHECKLIST_ITEM_ID already set")
    try:
        cur.execute("""ALTER TABLE INSPECTION_VIOLATION ADD FDID bigint FOREIGN KEY 
        REFERENCES FDID(FDID) """)
        conn.commit()
        print("FK INSPECTION_VIOLATION FDID set")
    except pyodbc.ProgrammingError as e:
        print("  FK INSPECTION_VIOLATION FDID already set")
    return


def init_inspection_violation_image_fk(conn, cur):
    try:
        cur.execute("""ALTER TABLE INSPECTION_VIOLATION_IMAGE ADD INSPECTION_VIOLATION_ID bigint FOREIGN KEY 
        REFERENCES INSPECTION_VIOLATION(INSPECTION_VIOLATION_ID) """)
        conn.commit()
        print("FK INSPECTION_VIOLATION_IMAGE INSPECTION_VIOLATION_ID set")
    except pyodbc.ProgrammingError as e:
        print("  FK INSPECTION_VIOLATION_IMAGE INSPECTION_VIOLATION_ID already set")
    try:
        cur.execute("""ALTER TABLE INSPECTION_VIOLATION_IMAGE ADD FDID bigint FOREIGN KEY 
        REFERENCES FDID(FDID) """)
        conn.commit()
        print("FK INSPECTION_VIOLATION_IMAGE FDID set")
    except pyodbc.ProgrammingError as e:
        print("  FK INSPECTION_VIOLATION_IMAGE FDID already set")
    return


def init_inspection_violation_status_fk(conn, cur):
    try:
        cur.execute("""ALTER TABLE INSPECTION_VIOLATION_STATUS ADD FDID bigint FOREIGN KEY 
        REFERENCES FDID(FDID) """)
        conn.commit()
        print("FK INSPECTION_VIOLATION_STATUS FDID set")
    except pyodbc.ProgrammingError as e:
        print("  FK INSPECTION_VIOLATION_STATUS FDID already set")
    return


def init_all(conn, cur):
    init_inspection_checklist_fk(conn, cur)
    init_inspection_checklist_item_fk(conn, cur)
    init_fire_code_fk(conn, cur)
    init_inspection_violation_fk(conn, cur)
    init_inspection_violation_image_fk(conn, cur)
    init_inspection_violation_status_fk(conn, cur)
    return
