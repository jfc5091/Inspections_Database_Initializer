import pyodbc

################################## PROPERTY #################################################


def init_property_fk(conn, cur):
    try:
        cur.execute("""ALTER TABLE PROPERTY ADD ADDRESS_ID bigint FOREIGN KEY 
        REFERENCES ADDRESS(ADDRESS_ID) """)
        conn.commit()
        print("FK PROPERTY ADDRESS_ID set")
    except pyodbc.ProgrammingError as e:
        print("  FK PROPERTY ADDRESS_ID already set")
    try:
        cur.execute("""ALTER TABLE PROPERTY ADD FDID bigint FOREIGN KEY 
        REFERENCES FDID(FDID) """)
        conn.commit()
        print("FK PROPERTY FDID set")
    except pyodbc.ProgrammingError as e:
        print("  FK PROPERTY FDID already set")
    return


def init_property_occupant_fk(conn, cur):
    try:
        cur.execute("""ALTER TABLE PROPERTY_OCCUPANT ADD ADDRESS_ID bigint FOREIGN KEY 
        REFERENCES ADDRESS(ADDRESS_ID) """)
        conn.commit()
        print("FK PROPERTY_OCCUPANT ADDRESS_ID set")
    except pyodbc.ProgrammingError as e:
        print("  FK PROPERTY_OCCUPANT ADDRESS_ID already set")
    try:
        cur.execute("""ALTER TABLE PROPERTY_OCCUPANT ADD PROPERTY_ID bigint FOREIGN KEY 
        REFERENCES PROPERTY(PROPERTY_ID) """)
        conn.commit()
        print("FK PROPERTY_OCCUPANT PROPERTY_ID set")
    except pyodbc.ProgrammingError as e:
        print("  FK PROPERTY_OCCUPANT PROPERTY_ID already set")
    try:
        cur.execute("""ALTER TABLE PROPERTY_OCCUPANT ADD FDID bigint FOREIGN KEY 
        REFERENCES FDID(FDID) """)
        conn.commit()
        print("FK PROPERTY_OCCUPANT FDID set")
    except pyodbc.ProgrammingError as e:
        print("  FK PROPERTY_OCCUPANT FDID already set")
    return


def init_property_owner_fk(conn, cur):
    try:
        cur.execute("""ALTER TABLE PROPERTY_OWNER ADD ADDRESS_ID bigint FOREIGN KEY 
        REFERENCES ADDRESS(ADDRESS_ID) """)
        conn.commit()
        print("FK PROPERTY_OWNER ADDRESS_ID set")
    except pyodbc.ProgrammingError as e:
        print("  FK PROPERTY_OWNER ADDRESS_ID already set")
    try:
        cur.execute("""ALTER TABLE PROPERTY_OWNER ADD PROPERTY_ID bigint FOREIGN KEY 
        REFERENCES PROPERTY(PROPERTY_ID) """)
        conn.commit()
        print("FK PROPERTY_OWNER PROPERTY_ID set")
    except pyodbc.ProgrammingError as e:
        print("  FK PROPERTY_OWNER PROPERTY_ID already set")
    try:
        cur.execute("""ALTER TABLE PROPERTY_OWNER ADD FDID bigint FOREIGN KEY 
        REFERENCES FDID(FDID) """)
        conn.commit()
        print("FK PROPERTY_OWNER FDID set")
    except pyodbc.ProgrammingError as e:
        print("  FK PROPERTY_OWNER FDID already set")
    return


def init_address_fk(conn, cur):
    try:
        cur.execute("""ALTER TABLE ADDRESS ADD ADDRESS_TYPE_ID bigint FOREIGN KEY 
        REFERENCES ADDRESS_TYPE(ADDRESS_TYPE_ID) """)
        conn.commit()
        print("FK ADDRESS ADDRESS_TYPE_ID set")
    except pyodbc.ProgrammingError as e:
        print("  FK ADDRESS ADDRESS_TYPE_ID already set")
    try:
        cur.execute("""ALTER TABLE ADDRESS ADD FDID bigint FOREIGN KEY 
        REFERENCES FDID(FDID) """)
        conn.commit()
        print("FK ADDRESS FDID set")
    except pyodbc.ProgrammingError as e:
        print("  FK ADDRESS FDID already set")
    return


def init_address_type_fk(conn, cur):
    try:
        cur.execute("""ALTER TABLE ADDRESS_TYPE ADD FDID bigint FOREIGN KEY 
        REFERENCES FDID(FDID) """)
        conn.commit()
        print("FK ADDRESS_TYPE FDID set")
    except pyodbc.ProgrammingError as e:
        print("  FK ADDRESS_TYPE FDID already set")
    return


def init_all(conn, cur):
    init_property_fk(conn, cur)
    init_property_occupant_fk(conn, cur)
    init_property_owner_fk(conn, cur)
    init_address_fk(conn, cur)
    init_address_type_fk(conn, cur)
    return
