import requests

Auth_Token = "NzY3MTMyMDYwMjkxOTU2ODA5.Gwp-_n.cMxwa0kJ62463wmZrP5X3tn5Bgy0edsg9eVjq0"
header = { "authorization": Auth_Token }

payload_data = { "type":2,
                 "application_id":"936929561302675456",
                 "channel_id":"1031056648250339358",
                 "session_id":"13cccca154f1265128351c19a71be8e6",
                 "data": { "version":"994261739745050686",
                           "id":"938956540159881230",
                           "name":"imagine",
                           "type":1,
                           "options": [ {  "type":3,
                                           "name":"prompt",
                                           "value":"Sun" 
                                        } ] 
                         }
               } 


class Handler:
    def _init_(self):
        pass

    def run_one_time(self):
        self.send_message_to_server()


    def send_message_to_server(self):
        r = requests.post(f"https://discord.com/api/v9/interactions", json=payload_data, headers=header)
        print(r.__dict__)


handler = Handler()
handler.run_one_time()