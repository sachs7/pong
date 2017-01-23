import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from download_xkcd import new_comic_number

email_from = <EMAIL ID>
recipients = <LIST of EMAIL IDs>
file_to_send = new_comic_number() + '.png'
username = email_from
password = <PASSWORD>

msg = MIMEMultipart()
msg['From'] = email_from
msg['bcc'] = ', '.join(recipients)
msg['Subject'] = 'XKCD comic # ' + new_comic_number()

''' Create's a file COMIC_RECORDS.TXT to hold the previous Comic's number, so that same comic should not be emailed to
recipients if there are no new comics.

If using cron job, provide complete path to the text files in below function.'''


def comic_ledger():
    with open('/give/complete/path/if/using/cron_job/comic_records.txt', 'r') as f:
        if new_comic_number() in f:
            print('SORRY! No new comics')
            return exit()
        else:
            with open('/give/complete/path/if/using/cron_job/comic_records.txt', 'w') as f:
                f.write(new_comic_number())


def attach_files():
    comic_ledger()
    with open(file_to_send, 'rb') as f:
        attachment = MIMEImage(f.read())
    attachment.add_header('Content-Disposition', 'attachment', filename=file_to_send)
    msg.attach(attachment)


def send_email():
    attach_files()
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(email_from, recipients, msg.as_string())
    server.quit()


if __name__ == '__main__':
    send_email()
