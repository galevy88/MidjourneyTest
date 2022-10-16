import requests

header = { "authorization": "NzY3MTMyMDYwMjkxOTU2ODA5.Gwp-_n.cMxwa0kJ62463wmZrP5X3tn5Bgy0edsg9eVjq0" }

dataA = { "type":3,
          "channel_id":"1031056648250339358",
          "message_flags":0,
          "message_id":"",
          "application_id":"936929561302675456",
          "session_id":"c84626dec94c2216b9c62061faf9f88f",
          "data": { "component_type":2,
                    "custom_id":"MJ::JOB::upsample::4::33a40aea-3e76-442b-9dc7-b90955506bab"
                    }
        }
dataB = {"type":3,"channel_id":"1031056648250339358","message_flags":0,"message_id":"1031083140237766666","application_id":"936929561302675456","session_id":"cb5bb351916439e691d1e4a257d8b0ce","data":{"component_type":2,"custom_id":"MJ::JOB::upsample::4::7cc4dfc3-aa6b-4bf1-b174-844667205b1f"}}
class Handler:
    def _init_(self):
        pass

    def run_one_time(self):
        self.send_message_to_server()


    def send_message_to_server(self):
        r = requests.post(f"https://discord.com/api/v9/interactions", json=dataB, headers=header)
        print(r.status_code)


handler = Handler()
handler.run_one_time()