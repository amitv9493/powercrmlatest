bind = "0.0.0.0:8000"
module = "powercrm.wsgi:application"

workers = 4  # Adjust based on your server's resources
worker_connections = 1000
threads = 4

certfile = "/etc/letsencrypt/live/engagepulse.com/fullchain.pem"
keyfile = "/etc/letsencrypt/live/engagepulse.com/privkey.pem"
