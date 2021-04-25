import pyodbc


################################## INSPECTIONS #################################################


def init_inspection_table(conn, cur):
    if cur.tables(table='INSPECTION', tableType='TABLE').fetchone():
        # if you add columns other than basic add here and add below
        print("  INSPECTION exists")
    else:
        cur.execute("""CREATE TABLE INSPECTION (
           INSPECTION_ID bigint NOT NULL IDENTITY(1,1) PRIMARY KEY,
           STATUS varchar(255),
           NARRATIVE ntext,
           OCCUPANT_SIGNATURE_URL ntext,
           INSPECTOR_SIGNATURE_URL ntext
           )""")
        print("INSPECTION created")
    conn.commit()
    return


def init_inspection_image_table(conn, cur):
    if cur.tables(table='INSPECTION_IMAGE', tableType='TABLE').fetchone():
        # if you add columns other than basic add here and add below
        print("  INSPECTION_IMAGE exists")
    else:
        cur.execute("""CREATE TABLE INSPECTION_IMAGE (
           INSPECTION_IMAGE_ID bigint NOT NULL IDENTITY(1,1) PRIMARY KEY,
           IMAGE_URL varchar(255)
           )""")
        print("INSPECTION_IMAGE created")
    conn.commit()
    return


def init_inspector_table(conn, cur):
    if cur.tables(table='INSPECTOR', tableType='TABLE').fetchone():
        # if you add columns other than basic add here and add below
        print("  INSPECTOR exists")
    else:
        cur.execute("""CREATE TABLE INSPECTOR (
           INSPECTOR_ID bigint NOT NULL IDENTITY(1,1) PRIMARY KEY,
           FIRST_NAME varchar(255),
           LAST_NAME varchar(255),
           PHONE varchar(255)
           )""")
        print("INSPECTOR created")
    conn.commit()
    return


def init_inspection_action_table(conn, cur):
    if cur.tables(table='INSPECTION_ACTION', tableType='TABLE').fetchone():
        # if you add columns other than basic add here and add below
        print("  INSPECTION_ACTION exists")
    else:
        cur.execute("""CREATE TABLE INSPECTION_ACTION (
           INSPECTION_ACTION_ID bigint NOT NULL IDENTITY(1,1) PRIMARY KEY,
           ACTION varchar(255),
           DATE datetime,
           DESCRIPTION varchar(255),
           NARRATIVE ntext
           )""")
        print("INSPECTION_ACTION created")
    conn.commit()
    return


def init_all(conn, cur):
    init_inspection_table(conn, cur)
    init_inspection_image_table(conn, cur)
    init_inspector_table(conn, cur)
    init_inspection_action_table(conn, cur)
    return

