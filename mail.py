import smtplib  #import SMTP lib

ss = smtplib.SMTP('smtp.gmail.com', 587)   #connect with GOOGLE SMTP

ss.starttls()                               #startServices
ss.login("Enter your Email id", "Enter your password")               #Enter Login Details

msg = "this is a testmail"                           #message you would like to attach      
ss.sendmail("Your Email id", "id you would like to send", msg)  
ss.quit()
