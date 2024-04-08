#!/usr/bin/env bash
# install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
            sudo apt-get update
                sudo apt-get install -y nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file for testing
echo "
<html>
        <head>
        </head>
        <body>
        Holberton School
        </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate symbolic link
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Set ownership recursively
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/^server {/a location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n}' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

exit 0
