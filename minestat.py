import minestat
import os
import time
from config import *
import sys
import requests
from discord import Webhook, RequestsWebhookAdapter
from datetime import datetime

if (int(duration)) < 1:
    duration = 30


dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%Y-%b-%d (%H:%M:%S)")
sleep = time.sleep(int(duration))

ms = minestat.MineStat(server_url, server_port)
if ms.online == True:
    status = 'online'

    ### Post to logs ###
    sourceFile = open('/minestat-logs/mc-server-logs.txt', 'a')
    print('**START**', file = sourceFile)
    print(server_online_msg , file = sourceFile)
    timestampStr = dateTimeObj.strftime("%Y-%b-%d (%H:%M:%S)")
    print('Server Status Change Time: ', timestampStr, file = sourceFile)
    print('**END**', file = sourceFile)
    print('/////////////', file = sourceFile)
    print(' ', file = sourceFile)
    sourceFile.close()
            
    ### Post to Discord webhook, server is online ###
    webhook = Webhook.from_url(discord_webhook, adapter=RequestsWebhookAdapter())
    if ping_init == 'no':
        webhook.send("Minecraft Server Monitoring is initiating... " + server_online_msg)
    else:
        webhook.send('@' + ping_role + " Minecraft Server Monitoring is initiating... " + server_online_msg)
    sleep


while 0 < 1:
    ms = minestat.MineStat(server_url, server_port)
    if ms.online == True:
        sleep
    else:
        status = 'offline'
        
        ### Post to logs ###
        sourceFile = open('/minestat-logs/mc-server-logs.txt', 'a')
        print('**START**', file = sourceFile)
        print(server_offline_msg , file = sourceFile)
        timestampStr = dateTimeObj.strftime("%Y-%b-%d (%H:%M:%S)")
        print('Server Status Change Time: ', timestampStr, file = sourceFile)
        print('**END**', file = sourceFile)
        print('/////////////', file = sourceFile)
        print(' ', file = sourceFile)
        sourceFile.close()

        ### Post to Discord webhook, server is offline ###
        webhook = Webhook.from_url(discord_webhook, adapter=RequestsWebhookAdapter())
        if ping_init == 'no':
            webhook.send(server_offline_msg)
        else:
            webhook.send('@' + ping_role + " " + server_offline_msg)
            

    while ms.online == None:
        status = 'offline'
        sleep
        ms = minestat.MineStat(server_url, server_port)
        if ms.online == True:
            status = 'online'
            
            ### Post to logs ###
            sourceFile = open('/minestat-logs/mc-server-logs.txt', 'a')
            print('**START**', file = sourceFile)
            print(server_online_msg , file = sourceFile)
            timestampStr = dateTimeObj.strftime("%Y-%b-%d (%H:%M:%S)")
            print('Server Status Change Time: ', timestampStr, file = sourceFile)
            print('**END**', file = sourceFile)
            print('/////////////', file = sourceFile)
            print(' ', file = sourceFile)
            sourceFile.close()
            
            ### Post to Discord webhook, server is online ###
            webhook = Webhook.from_url(discord_webhook, adapter=RequestsWebhookAdapter())
            if ping_init == 'no':
                webhook.send(server_online_msg)
            else:
                webhook.send('@' + ping_role + " " + server_online_msg)
            sleep
