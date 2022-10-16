
import requests
import json


class Handler:
    def __init__(self):
        self.header = self.genrate_header()
        self.current_image_url = ""
        self.channel_id = "765498417904353306"

    def run_one_time(self):
        self.achive_image_url()
        # self.send_message_to_server("Start Execute")
        # self.send_message_to_server("Acheiving Image URL")
        # self.send_message_to_server("Finish Execute Code:0")
        self.send_message_to_server(self.current_image_url)
        


    def genrate_header(self):
        header = { "authorization": "NzY3MTMyMDYwMjkxOTU2ODA5.Gwp-_n.cMxwa0kJ62463wmZrP5X3tn5Bgy0edsg9eVjq0" }
        return header

    def generate_payload(self, message):
        payload = { "content": message }
        return payload

    def send_message_to_server(self, message):
        payload = self.generate_payload(message)
        r = requests.post(f"https://discord.com/api/v9/interactions", channel, headers=self.header)

    def achive_image_url(self):
        binaryPayload = requests.get(f"https://discord.com/api/v9/channels/{self.channel_id}/messages", headers=self.header)
        print(binaryPayload.content)
        extractedData = json.loads(binaryPayload.content)
        print(json.dumps(extractedData, indent=2))
        lastMessageData = extractedData[0]
        attachments = lastMessageData["attachments"][0]
        imageURL = attachments["url"]
        self.current_image_url = imageURL
        print(json.dumps(imageURL, indent=2))


handler = Handler()
handler.run_one_time()
