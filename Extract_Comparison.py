from emailTest113 import Create_Email
from dbfunc import Database_Connect, Query_Call
import smtplib


if __name__ == '__main__':

    database = 'mydb.employee'
    cursor = Database_Connect('localhost', 'mydb', 'root', 'rabel1986')
    result = Query_Call(cursor, database)

    for obj in result:
        data = obj[0]
        print(obj)
    message = Create_Email(data)

    try:
        smtp_host = smtplib.SMTP("smtp.office365.com", 587)
        smtp_host.ehlo()
        smtp_host.starttls()
        smtp_host.login("dominicandaddy_nyc@hotmail.com", 'rdc_23?')
        smtp_host.sendmail("dominicandaddy_nyc@hotmail.com", "rabeldelcastillo23@gmail.com", message.as_string())
        smtp_host.quit()

        print("Success")
    except:
        print("Failed")
