
import smtplib


def send_email():
    """sends an email when the data sanitation is not passed"""
    
    smtp_server = 'smtp.west.com'
    from_address = 'dwteam@west.com'

    to_address = 'afarias@west.com'

    text = "the records missing from the file exceed 25%."

    server = smtplib.SMTP(smtp_server, 25)
    server.ehlo()
    server.starttls()
    server.sendmail(from_address, to_address, text)

    server.quit()




send_email()
