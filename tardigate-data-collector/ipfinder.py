import redis
import os
from dotenv import load_dotenv
load_dotenv()

pool = redis.ConnectionPool(host=os.getenv("redis_host"), port=os.getenv("redis_port"), db=0)

r = redis.Redis(connection_pool=pool)

def findIp(Ip):
    status = r.get(Ip)
    if status:
        return False
    else: 
        return True

def seed():
     f = open("full_blacklist_database.txt", "r")
     text = f.read()
     text = text.splitlines()
     for i in range(len(text)):
        text[i] = text[i].split('\t\t\t')[0]
        r.set(text[i],1)
        print("key seeded")
     
