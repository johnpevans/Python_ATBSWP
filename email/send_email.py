import smtplib

email = input('What is your email:')
password = input('What is your password for your email:')
toEmail = input('Who do you want to send an email too:')
header = input('What is the subject header:')
salutation = input('Dear: ')
message = input('Message:')
signature = input('Sincerely:')

conn = smtplib.SMTP('smtp.gmail.com', 587)
type(conn)
conn.ehlo()#starts the connections
conn.starttls()
conn.login(email,password)
conn.sendmail(email, toEmail,
'Subject:{0}..\n\nDear {1},\n\n {2}\n\n Sincerely,\n {3}'.format(header,
    salutation, message, signature))

conn.quit()
