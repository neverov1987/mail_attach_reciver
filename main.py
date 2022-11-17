from imap_tools import MailBox, A
import subprocess
import time
import os

botToken = os.getenv('TOKEN')
chat_id = os.environ.get('CHAT_ID')
attachments_dir = '/tmp/{}'
mail_server = os.getenv('MAIL_SERVER')
mail_login = os.environ.get('MAIL_LOGIN')
mail_password = os.getenv('MAIL_PASSWORD')
mail_folder = os.getenv('MAIL_FOLDER')


def get_attachment(server, login, password, folder, att_dir):
    with MailBox(server).login(login, password, folder) as mailbox:
       for msg in mailbox.fetch(A(seen=False)):
           for att in msg.attachments:
               if att.content_type == 'image/jpeg':
                   with open(att_dir.format(att.filename), 'wb') as f:
                       file_name = str(att_dir.format(att.filename))
                       f.write(att.payload)
                   send_image(botToken, chat_id, file_name)
                   os.remove(file_name)
               else:
                   print('Attach is not image')


def send_image(botToken, chat_id, imageFile):
    command = 'curl -s -X POST https://api.telegram.org/bot' + botToken + '/sendPhoto -F chat_id=' + chat_id + " -F photo=@" + imageFile
    subprocess.call(command.split(' '))
    return


while True:
  get_attachment(mail_server, mail_login, mail_password, mail_folder, attachments_dir)
  time.sleep(30)