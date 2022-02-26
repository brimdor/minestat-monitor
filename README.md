# Minestat Monitor
Core Code - Minestat from FragLand [https://github.com/FragLand/minestat]

I added the ability for you to customize your Minecraft Server Info and allow it monitor the server which will send a webhook when the status changes.


Status Changes:
1. Initial start of the app declares if server is online or offline.
2. Server is online
3. Server is offline


Before the app can function, you will need to do the following:
1. Update the config.py
2. If you plan to run the app in a container you can edit the Docker Sample Command and run it within your Docker environment.
3. If you plan to run it standalone, download the app files to a designated folder on your system then run it using Python 3 with the following command 'python minestat.py'

----------

Docker Sample Command:
`docker run -dit --name call it what you want -e server_url='x.x.x.x' -e server_port='25565' -e duration='5' -e ping_role='role-name' -e webhook_url='webhook-url' -v host/log/location:/minestat-logs brimdor/minestat:latest`

