import smtplib
from cred import my_mail,my_pwd

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login ("kakanurusucharitha@gmail.com", my_pwd)
msg = "please subscribe to my channel"
reciever_mail ="kvinaykumarreddy1995@gmail.com"
s.send_mail(my_mail,reciever_mail,msg)
s.quit()
print("successsfully sent")
