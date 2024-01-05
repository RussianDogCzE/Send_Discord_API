import requests # Install requests

url = "https://discord.com/api/v9/channels/CHANNELID/messages" # Change "CHANNELID" to the ID channel
input_msg = input("Send: ")

for i in range(1): # If you want to spam, change to 500 or 1000
    payload = {
        "content" : f"{input_msg}"
    }

    headers = {
        "Authorization" : "token" # Change to your token, trust me :)
    }

    res = requests.post(url, payload, headers=headers)