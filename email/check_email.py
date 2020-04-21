#! python3
import pyzmail, imapclient

conn = imapclient.IMAPClient('imaps.google.com.com', ssl=True)

conn.login('','')
conn.select_folder('INBOX', readonly = True)

UIDs = conn.search(['SINCE20-Aug-2015'])

rawMessage = conn.fetch([UIDs],['BODY[]','FLAGS'])
message = pyzmail.PyzMessage.factory(rawMEssage[UIDs[b'BODY[]']])

message.get_subject()
message.get_address('from')
message.text_part.get_payload().decode('UTF-8')
message.text_part.charset == None

conn.list_folders()
conn.select_folder('INBOX', readonly = False)

UIDS = conn.search(['ON DATE'])


#Can look up unread emails and do a count
