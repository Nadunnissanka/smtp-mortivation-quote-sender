# import smtplib first
import smtplib

my_email = "nadunnissanka@yahoo.com"
my_password = "kbbzybtjgoqlrvsp"

with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="chamika.2018101@iit.ac.lk",
        msg="Subject:Hi Chamika Chiran\n\nThis is a generated message from python smtplib! Hello Please ignore this msg."
    )
