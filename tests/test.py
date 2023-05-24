import requests

url = "http://10.1.17.217/RSAarcher/api/core/content/multipartattachment"
bt = open("")
payload = {
"AttachmentName":"Bodie.jpg",
"AttachmentBytes":"/9j/4AAQSkZJRgABAgAAAQABAAD/4QDmRXhpZgAASUkqA
AgAAAAFABIBAwABAAAAAQAAADEBAgAcAAAASgAAADIBAgAUA
AAAZgAAABMCAwABAAAAAQAAAGmHBAABAAAAegAAAAAAAABBQ0QgU3lzdGVtcyBEa
WdpdGFsIE"
}
headers = {
    'Accept': 'application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Authorization': 'Archer session-id=58E02925B18ADE85A5A86B11A30BF0CE'
}

response = requests.request(
    "POST", url, headers=headers, data=payload, files=files)

print(response.text)
