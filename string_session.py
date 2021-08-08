from pyrogram import Client

ryoko = ''' 
 ______                _           
 | ___ \              | |          
 | |_/ / _   _   ___  | | __  ___  
 |    / | | | | / _ \ | |/ / / _ \ 
 | |\ \ | |_| || (_) ||   < | (_) |
 \_| \_| \__, | \___/ |_|\_\ \___/ 
          __/ |                    
         |___/                     
'''

print(ryoko)

API_KEY = int(input("Enter API KEY: "))
API_HASH = input("Enter API HASH: ")
with Client(":memory:", api_id=API_KEY, api_hash=API_HASH) as app:
    print(app.export_session_string())
