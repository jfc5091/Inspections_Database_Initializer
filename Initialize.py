import pandas as pd
import pyodbc

from tables import init_table_audit_logs as audit_logs
from tables import init_table_checklist as checklist
from tables import init_table_fdid as fdid
from tables import init_table_inspection as inspection
from tables import init_table_property as properties
from tables import init_table_users as users

# cur.execute("""if not exists (select
#                    column_name
#            from
#                    INFORMATION_SCHEMA.columns
#            where
#                  table_name = 'NFIRS_ATT'
#                   and column_name = 'INC_NUM')
#                         alter table NFIRS_ATT add INC_NUM varchar(255)""")

################################## TABLES ##############################################################




################################## MAIN ROUTINE #################################################


def init_tables(conn,cur):

    audit_logs.init_all(conn, cur)
    checklist.init_all(conn, cur)
    fdid.init_all(conn, cur)
    inspection.init_all(conn, cur)
    properties.init_all(conn, cur)
    users.init_all(conn, cur)
    return


def main():
    """
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                          'Server=DESKTOP-69SKM75\SQLEXPRESS;'
                          'PORT=1433;'
                          'DATABASE=INSPECTIONS;'
                          'UID=frtAdmin;'
                          'PWD=TurtleTeacher4ever;')
    """
    """
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-MCPJ4LG;'
                      'Database=INSPECTIONS;'
                      'PORT=1433;'
                      'UID=FireRMS;'
                      'PWD=FireAdmin;')
    """

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-69SKM75\SQLEXPRESS;'
                          'Database=INSPECTIONS;'
                          'UID=frtAdmin;'
                          'PWD=TurtleTeacher4ever;'
                          'Trusted_Connection=yes;')

    # conn = pyodbc.connect('Driver={SQL Server};Server=tcp:inspection.database.windows.net,1433;Database=INSPECTIONS;Uid=jfc5091;Pwd=superb!Drift&tune;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')

    cur = conn.cursor()
    init_tables(conn, cur)
    cur.close()
    conn.commit()
    conn.close()
    return


if __name__ == "__main__":
    main()
