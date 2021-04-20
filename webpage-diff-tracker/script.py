import requests
import smtplib
from email.message import EmailMessage
import hashlib
from urllib.request import urlopen
from datetime import date
import json
from os import listdir
from os.path import isfile, join


change_msgs= []
error_msgs=[]
data = json.loads(open("./data.json").read())
password=data["from-password"]
sender=data["from-email"]
recipient=data["to-email"]
urls=data["urls"]
hashes=[]
for url in urls:
    hashes.append(hashlib.sha224(url.encode('utf-8')).hexdigest())
files = [f for f in listdir('./hashes') if isfile(join('./hashes', f))]

for i in range(len(urls)):
    path_to_hash="./hashes/"+hashes[i]+".txt"
    url=urls[i]     
    try:
        if(hashes[i]+'.txt' not in files):
            print(url+" "+hashes[i]+" : New URL found...")
            f=open(path_to_hash,'wt')
            response = urlopen(url).read()
            newHash = hashlib.sha224(response).hexdigest()
            f.write(newHash)
            f.close()
            continue
        response = urlopen(url).read()
        #print(response)
        currentHash = hashlib.sha224(response).hexdigest()
        f = open(path_to_hash)
        currentHash=f.readline()
        f.close()
        response = urlopen(url).read()
        newHash = hashlib.sha224(response).hexdigest()
        if(currentHash==""):
            print(url+" "+hashes[i]+" : Hash was not stored earlier. Creating new hash")
            f=open(path_to_hash,'wt')
            f.write(newHash)
            f.close()
            continue
        if newHash == currentHash:
            print(url+" "+hashes[i]+" : Hash Matched. No changes in webpage structure.")

        else:
            print(url+" "+hashes[i]+" : Hash did not matched")
            f=open(path_to_hash,'wt')
            f.write(newHash)
            f.close()
            print("Stored the Hash for next iteration..\n Composing email...")
            change_msgs+=[url]
        # error_msgs+=[url+" This is sample error"]
    except Exception as e:
        msg = EmailMessage()
        msg.set_content("Some error Occured" + str(e)+url)
        error_msgs+=[url+str(e)]

if(len(change_msgs)!=0 or len(error_msgs)!=0):
    mail=EmailMessage()
    mail['From']=sender
    mail['To']=recipient
    subject=str(date.today().strftime("%b-%d-%Y"))
    message=""
    if(len(change_msgs)!=0):
        subject+=' | '+str(len(change_msgs))+" changes"
        message+="Changes:\n"
        for i in range(len(change_msgs)):
            message+=str(i+1)+". "+str(change_msgs[i])+'\n'
    if(len(error_msgs)!=0):
        subject+=' | '+str(len(error_msgs))+" errors"
        message+="Errors:\n"
        for i in range(len(error_msgs)):
            message+=str(i+1)+". "+str(error_msgs[i])+'\n'
    mail['Subject']=subject
    print(subject)
    print(message)
    mail.add_alternative(message)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender, password)
    server.send_message(mail)
    print(mail)
    print("sent")
    server.quit()