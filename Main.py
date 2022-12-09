# import threading
# import time
# from datetime import datetime
#
# import mysql.connector
# import schedule
#
# import accessControl12
# from accessControl12 import Ui_MainWindow
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='sakerimene007',
#     port='3306',
#     database='controling_entrance'
# )
#
# mycursor = mydb.cursor(buffered=True)
#
# def control(lp):
#
#     now = datetime.now()
#     mycursor.execute("SELECT licence_plate FROM knowing_plate WHERE licence_plate="+lp+";")
#     db = mycursor.fetchone()
#     if db is None:
#         print("There is no licence plate like this in the knowing plate ")
#         mycursor.execute("SELECT licence_plate FROM visitor WHERE licence_plate = " + lp + ";")
#         check = mycursor.fetchone()
#         if check is None:
#             now = datetime.now()
#             et = now.strftime('%Y-%m-%d %H:%M:%S')
#             ext = None
#             mycursor.execute(" INSERT INTO visitor ("
#                              "licence_plate,"
#                              "entrance_time,"
#                              "exit_time)"
#                              "VALUES(%s,%s,%s)", (lp, et, ext))
#             print("Visitor table :")
#             mycursor.execute("SELECT * FROM visitor ")
#             visitors = mycursor.fetchall()
#             for visitor in visitors:
#                 print(visitor)
#
#         else:
#             now = datetime.now()
#             ext = now.strftime('%Y-%m-%d %H:%M:%S')
#             mycursor.execute("DELETE FROM visitor WHERE licence_plate = " + lp + ";")
#             print("Visitor table:")
#             mycursor.execute("SELECT * FROM visitor ")
#             visitors = mycursor.fetchall()
#             for visitor in visitors:
#                 print(visitor)
#
#
#
#         mycursor.execute("SELECT licence_plate FROM control_access WHERE licence_plate = "+lp+" ;")
#         checkControl = mycursor.fetchone()
#         if checkControl is None:
#             print("there is no plate in access")
#             now = datetime.now()
#             et = now.strftime('%Y-%m-%d %H:%M:%S')
#             ext = None
#             case = "V"
#             mycursor.execute("INSERT INTO control_access ( "
#                                  "licence_plate,"
#                                  "entrance_time,"
#                                  "exit_time,"
#                                  "case_A_V)"
#                                  "VALUES(%s,%s,%s,%s);", (lp, et, ext, case))
#             print("Control access table :")
#             mycursor.execute("SELECT * FROM control_access ;")
#             control = mycursor.fetchall()
#             for access in control:
#                 print(access)
#
#         else:
#             now = datetime.now()
#             ext = now.strftime('%Y-%m-%d %H:%M:%S')
#             mycursor.execute("UPDATE control_access SET exit_time ='" + ext + "' WHERE licence_plate ='" + lp + "';")
#             print("Control access table :")
#             mycursor.execute("SELECT * FROM control_access; ")
#             controls = mycursor.fetchall()
#             for access in controls:
#                 print(access)
#
#
#
#
#     else:
#         full = 1
#         for user in db:
#             if user == lp:
#                 case = "A"
#                 print(user)
#                 print("licence plate autorised ")
#                 print("Knowing plate table :")
#                 mycursor.execute("SELECT * FROM knowing_plate WHERE licence_plate=" + lp + ";")
#                 select = mycursor.fetchone()
#                 for allData in select:
#                     print(allData)
#                 print("Control access table :")
#                 now = datetime.now()
#                 et = now.strftime('%Y-%m-%d %H:%M:%S')
#                 ext = None
#                 mycursor.execute("SELECT licence_plate FROM control_access WHERE licence_plate = " + lp + " ;")
#                 checkControl = mycursor.fetchone()
#                 if checkControl is None:
#                     now = datetime.now()
#                     et = now.strftime('%Y-%m-%d %H:%M:%S')
#                     ext = None
#                     mycursor.execute("INSERT INTO control_access ( "
#                                      "licence_plate,"
#                                      "entrance_time,"
#                                      "exit_time,"
#                                      "case_A_V)"
#                                      "VALUES(%s,%s,%s,%s);", (lp, et, ext, case))
#                     print("Control access table :")
#                     mycursor.execute("SELECT * FROM control_access ;")
#                     control = mycursor.fetchall()
#                     for access in control:
#                         print(access)
#                         th = threading.Thread(target=fill, args=())
#                         th.start()
#                 else:
#                     now = datetime.now()
#                     ext = now.strftime('%Y-%m-%d %H:%M:%S')
#                     mycursor.execute(
#                         "UPDATE control_access SET exit_time ='" + ext + "' WHERE licence_plate ='" + lp + "';")
#                     print("Control access table :")
#                     mycursor.execute("SELECT * FROM control_access; ")
#                     controls = mycursor.fetchall()
#                     for access in controls:
#                         print(access)
#
#     mydb.commit()
#
# #def app():
#  #   accessControl12.main()
#
# #th = threading.Thread(target= app, args=())
# #th.start()