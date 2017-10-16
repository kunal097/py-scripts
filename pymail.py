import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

username=input("Enter email address : ")
password=getpass.getpass()
host="smtp.gmail.com"
port=587
from_email=username
to_list=[]

n=int(input("Enter no. of reciptents : "))
i=0
while i<n:
	to_list.append(input())
	i+=1

email_conn=smtplib.SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username,password)

msg=MIMEMultipart("alternative")
msg["Subject"]=input("Enter Subject : ")
msg["From"]=username	

con=input("Enter content : ")

html_txt= """\
          <html>
             <head></head>
             <body><p>Hey There !!<br>"""+con+"""</p></body>
          </html>
          """

p2=MIMEText(html_txt,"html")
msg.attach(p2)


email_conn.sendmail(from_email,to_list,msg.as_string())
email_conn.quit()


