[![Docker Image CI](https://github.com/neverov1987/mail_attach_reciver/actions/workflows/docker-image.yml/badge.svg?branch=master)](https://github.com/neverov1987/mail_attach_reciver/actions/workflows/docker-image.yml) <br />
Run example:
```
MY_IMAGE_NAME=neverov1987/mail_attach_reciver
docker build -t $MY_IMAGE_NAME .
docker run -ti \
    -e TOKEN="XXXXXX:yyyyyyy..." \
    -e CHAT_ID="ZZZZZZZZZ" \
    -e MAIL_SERVER='<your_imap_server_address>' \
    -e MAIL_LOGIN='<your_mail_login>>' \
    -e MAIL_PASSWORD='your_mail_password' \
    -e MAIL_FOLDER='<folder for search attachments>' \ #By default Inbox
    -e MAIL_CHECK_INTERVAL='30' \ #By default 30 sec
$MY_IMAGE_NAME
```
