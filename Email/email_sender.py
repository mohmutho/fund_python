import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Bima'
email['to'] = 'mohammad.mutho@gmail.com'
email['subject'] = 'Selamat Menjalani Masa Karantina Tho'

email.set_content('Nyoba Email Sender!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp :
    smtp.ehlo()
    smtp.starttls()
    smtp.login('bimarachmat24@gmail.com', 'C4hritula')
    smtp.send_message(email)
    print('all done!')