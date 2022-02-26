import os

#NOTE: if you are not using Environment Variables, you will need to set the variables in this config file.

#minecraft server info
if os.environ.get('server_url') == None:
    server_url = '<set default>' #Set This
else:
    server_url = os.environ['server_url']

if os.environ.get('server_port') == None:
    server_port = 25565 #Set This. Defaulted to the Java Server default port.
else:
    server_port =  (int(os.environ['server_port']))

#time between health checks (minimum 1 second, default 30 seconds, 0 = default)
if os.environ.get('duration') == None:
    duration = 30 #Set This if you don't want default
else:
    duration = (int(os.environ['duration']))

#Would you like to be able to ping a specific role? (yes, no)
if os.environ.get('ping_init') == None:
    ping_init = 'no' #Default is No
else:
    ping_init = os.environ['ping_init']

#Role you would you like to inform on the server
if os.environ.get('ping_role') == None:
    ping_role = '<the role>' #Set This
else:
    ping_role = os.environ['ping_role']
    
#discord webhook url
if os.environ.get('discord_webhook') == None:
    discord_webhook = '<webhook url>' #Set This
else:
    discord_webhook = os.environ['discord_webhook']

#Offline Message
if os.environ.get('server_offline_msg') == None:
    server_offline_msg = 'The Server is Offline!' #Set This
else:
    server_offline_msg = os.environ['server_offline_msg']

#Online Message
if os.environ.get('server_online_msg') == None:
    server_online_msg = 'The Server is Online!' #Set This
else:
    server_online_msg = os.environ['server_online_msg']