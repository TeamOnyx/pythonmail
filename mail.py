import smtplib

ss = smtplib.SMTP('smtp.gmail.com', 587)
ss.starttls()
ss.login("yourid", "yourpass")

msg = "this is a testmail"
ss.sendmail("yourid", "id you would like to send", msg)
ss.quit()
