import pyodbc

from foreign_keys import init_fk_audit_logs as audit_logs
from foreign_keys import init_fk_checklist as checklist
from foreign_keys import init_fk_inspection as inspection
from foreign_keys import init_fk_property as properties
from foreign_keys import init_fk_users as users

def init_fk(conn, cur):

    audit_logs.init_all(conn, cur)
    checklist.init_all(conn, cur)
    inspection.init_all(conn, cur)
    properties.init_all(conn, cur)
    users.init_all(conn, cur)
    return


def main():
    """
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                          'Server=firstresponsetesting.database.windows.net;'
                          'PORT=1433;'
                          'DATABASE=INSPECTIONS;'
                          'UID=frtAdmin;'
                          'PWD=TurtleTeacher4ever;')
    """
    """
        conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-69SKM75\SQLEXPRESS;'
                          'Database=INSPECTIONS;'
                          'UID=frtAdmin;'
                          'PWD=TurtleTeacher4ever;'
                          'Trusted_Connection=yes;')
    """

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-69SKM75\SQLEXPRESS;'
                          'Database=INSPECTIONS;'
                          'UID=frtAdmin;'
                          'PWD=TurtleTeacher4ever;'
                          'Trusted_Connection=yes;')

    # conn = pyodbc.connect('Driver={SQL Server};Server=tcp:inspection.database.windows.net,1433;Database=INSPECTIONS;Uid=jfc5091;Pwd=superb!Drift&tune;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cur = conn.cursor()
    init_fk(conn, cur)
    cur.close()
    conn.commit()
    conn.close()
    return



if __name__ == "__main__":
    main()

