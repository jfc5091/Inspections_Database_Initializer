import pyodbc

################################## PROPERTY #################################################


def init_property_table(conn, cur):
    if cur.tables(table='PROPERTY', tableType='TABLE').fetchone():
        # if you add columns other than basic add here and add below
        print("  PROPERTY exists")
    else:
        cur.execute("""CREATE TABLE PROPERTY (
           PROPERTY_ID bigint NOT NULL IDENTITY(1,1) PRIMARY KEY
           )""")
        print("PROPERTY created")
    conn.commit()
    return


def init_property_occupant_table(conn, cur):
    if cur.tables(table='PROPERTY_OCCUPANT', tableType='TABLE').fetchone():
        # if you add columns other than basic add here and add below
        print("  PROPERTY_OCCUPANT exists")
    else:
        cur.execute("""CREATE TABLE PROPERTY_OCCUPANT (
           PROPERTY_OCCUPANT_ID bigint NOT NULL IDENTITY(1,1) PRIMARY KEY,
           FIRST_NAME varchar(255),
           LAST_NAME varchar(255),
           PHONE varchar(255),
           EMAIL ntext,
           FAX varchar(255),
           )""")
        print("PROPERTY_OCCUPANT created")
    conn.commit()
    return


def init_property_owner_table(conn, cur):
    if cur.tables(table='PROPERTY_OWNER', tableType='TABLE').fetchone():
        # if you add columns other than basic add here and add below
        print("  PROPERTY_OWNER exists")
    else:
        cur.execute("""CREATE TABLE PROPERTY_OWNER (
           PROPERTY_OWNER_ID bigint NOT NULL IDENTITY(1,1) PRIMARY KEY,
           FIRST_NAME varchar(255),
           LAST_NAME varchar(255),
           PHONE varchar(255),
           EMAIL ntext,
           FAX varchar(255),
           )""")
        print("PROPERTY_OWNER created")
    conn.commit()
    return


def init_address_table(conn, cur):
    if cur.tables(table='ADDRESS', tableType='TABLE').fetchone():
        # if you add columns other than basic add here and add below
        print("  ADDRESS exists")
    else:
        cur.execute("""CREATE TABLE ADDRESS (
           ADDRESS_ID bigint NOT NULL IDENTITY(1,1) PRIMARY KEY,
           ADDRESS_LINE1 varchar(255),
           ADDRESS_LINE2 varchar(255),
           CITY varchar(255),
           STATE varchar(255),
           ZIP varchar(255),
           LONGITUDE decimal(9,6),
           LATITUDE decimal(9,6),
           ENABLED bit
           )""")
        print("ADDRESS created")
    conn.commit()
    return


def init_address_type_table(conn, cur):
    if cur.tables(table='ADDRESS_TYPE', tableType='TABLE').fetchone():
        # if you add columns other than basic add here and add below
        print("  ADDRESS_TYPE exists")
    else:
        cur.execute("""CREATE TABLE ADDRESS_TYPE (
           ADDRESS_TYPE_ID bigint NOT NULL IDENTITY(1,1) PRIMARY KEY,
           TYPE varchar(255),
           ENABLED bit
           )""")
        print("ADDRESS_TYPE created")
    conn.commit()
    return


def init_all(conn, cur):
    init_property_table(conn, cur)
    init_property_occupant_table(conn, cur)
    init_property_owner_table(conn, cur)
    init_address_table(conn, cur)
    init_address_type_table(conn, cur)
    return
