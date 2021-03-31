import pyodbc

################################## CHECKLISTS #################################################


def init_inspection_checklist_table(conn, cur):
    if cur.tables(table='INSPECTION_CHECKLIST', tableType='TABLE').fetchone():
        # if you add columns other than basic add here and add below
        print("  INSPECTION_CHECKLIST exists")
    else:
        cur.execute("""CREATE TABLE INSPECTION_CHECKLIST (
           INSPECTION_CHECKLIST_ID bigint NOT NULL IDENTITY(1,1) PRIMARY KEY,
           TYPE varchar(255),
           ENABLED bit
           )""")
        print("INSPECTION_CHECKLIST created")
    conn.commit()
    return


def init_inspection_checklist_item_table(conn, cur):
    if cur.tables(table='INSPECTION_CHECKLIST_ITEM', tableType='TABLE').fetchone():
        # if you add columns other than basic add here and add below
        print("  INSPECTION_CHECKLIST_ITEM exists")
    else:
        cur.execute("""CREATE TABLE INSPECTION_CHECKLIST_ITEM (
           INSPECTION_CHECKLIST_ITEM_ID bigint NOT NULL IDENTITY(1,1) PRIMARY KEY,
           DESCRIPTION varchar(255)
           )""")
        print("INSPECTION_CHECKLIST_ITEM created")
    conn.commit()
    return


def init_inspection_checklist_item_status_table(conn, cur):
    if cur.tables(table='INSPECTION_CHECKLIST_ITEM_STATUS', tableType='TABLE').fetchone():
        # if you add columns other than basic add here and add below
        print("  INSPECTION_CHECKLIST_ITEM_STATUS exists")
    else:
        cur.execute("""CREATE TABLE INSPECTION_CHECKLIST_ITEM_STATUS (
           INSPECTION_CHECKLIST_ITEM_STATUS_ID bigint NOT NULL IDENTITY(1,1) PRIMARY KEY,
           STATUS varchar(255)
           )""")
        print("INSPECTION_CHECKLIST_ITEM_STATUS created")
    conn.commit()
    return


def init_fire_code_table(conn, cur):
    if cur.tables(table='FIRE_CODE', tableType='TABLE').fetchone():
        # if you add columns other than basic add here and add below
        print("  FIRE_CODE exists")
    else:
        cur.execute("""CREATE TABLE FIRE_CODE (
           FIRE_CODE_ID bigint NOT NULL IDENTITY(1,1) PRIMARY KEY,
           CODE varchar(255),
           DESCRIPTION varchar(255),
           ENABLED bit
           )""")
        print("FIRE_CODE created")
    conn.commit()
    return


def init_inspection_violation_table(conn, cur):
    if cur.tables(table='INSPECTION_VIOLATION', tableType='TABLE').fetchone():
        # if you add columns other than basic add here and add below
        print("  INSPECTION_VIOLATION exists")
    else:
        cur.execute("""CREATE TABLE INSPECTION_VIOLATION (
           INSPECTION_VIOLATION_ID bigint NOT NULL IDENTITY(1,1) PRIMARY KEY,
           DESCRIPTION varchar(255),
           LOCATION varchar(255),
           NARRATIVE ntext,
           DATE_FOUND datetime,
           ABATE_DATE datetime,
           DATE_CORRECTED datetime
           )""")
        print("INSPECTION_VIOLATION created")
    conn.commit()
    return


def init_inspection_violation_image_table(conn, cur):
    if cur.tables(table='INSPECTION_VIOLATION_IMAGE', tableType='TABLE').fetchone():
        # if you add columns other than basic add here and add below
        print("  INSPECTION_VIOLATION_IMAGE exists")
    else:
        cur.execute("""CREATE TABLE INSPECTION_VIOLATION_IMAGE (
           INSPECTION_VIOLATION_IMAGE_ID bigint NOT NULL IDENTITY(1,1) PRIMARY KEY,
           IMAGE_URL ntext
           )""")
        print("INSPECTION_VIOLATION_IMAGE created")
    conn.commit()
    return


def init_inspection_violation_status_table(conn, cur):
    if cur.tables(table='INSPECTION_VIOLATION_STATUS', tableType='TABLE').fetchone():
        # if you add columns other than basic add here and add below
        print("  INSPECTION_VIOLATION_STATUS exists")
    else:
        cur.execute("""CREATE TABLE INSPECTION_VIOLATION_STATUS (
           INSPECTION_VIOLATION_STATUS_ID bigint NOT NULL IDENTITY(1,1) PRIMARY KEY,
           STATUS varchar(255)
           )""")
        print("INSPECTION_VIOLATION_STATUS created")
    conn.commit()
    return


def init_all(conn, cur):
    init_inspection_checklist_table(conn, cur)
    init_inspection_checklist_item_table(conn, cur)
    init_inspection_checklist_item_status_table(conn, cur)
    init_fire_code_table(conn, cur)
    init_inspection_violation_table(conn, cur)
    init_inspection_violation_image_table(conn, cur)
    init_inspection_violation_status_table(conn, cur)
    return
