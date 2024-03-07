import smtplib

def send(self_email,reciever_email, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587) #port 465 or 587
    server.starttls() 

    server.login(self_email, "cffs ehnp wlca sxwd")

    server.sendmail(self_email, reciever_email, f"Subject: {subject}\n\n{message}")

    print("EMAIL HAS BEEN SENT SUCCESSFULLY")
   
