#!/bin/bash -u

echo PUBLIC_HOSTNAME is ${PUBLIC_HOSTNAME:=$(curl http://169.254.169.254/latest/meta-data/public-hostname)}
echo PORT is ${PORT:=8080}

cd /etc/rundeck/

#:edit rundeck-config.properties
if [ ! -f rundeck-config.properties.bak ]; then
    cp -p rundeck-config.properties rundeck-config.properties.bak
fi
echo "grails.serverURL=http://${PUBLIC_HOSTNAME}:${PORT}" > /tmp/serverURL.txt
cat rundeck-config.properties.bak \
    | sed -e '/grails.serverURL/r /tmp/serverURL.txt' -e '/grails.serverURL/d' \
    > rundeck-config.properties
diff rundeck-config.properties rundeck-config.properties.bak

#:edit framework.properties
if [ ! -f framework.properties.bak ]; then
    cp -p framework.properties framework.properties.bak
fi
echo "framework.server.url = http://${PUBLIC_HOSTNAME}:${PORT}" > /tmp/framework_server_url.txt
cat framework.properties.bak \
    | sed -e "s/localhost/${PUBLIC_HOSTNAME}/g" \
            -e "s/4440/${PORT}/g" \
    > framework.properties
diff framework.properties framework.properties.bak

echo "To verify that the service started correctly, tail the logs:"
echo "tail -f /var/log/rundeck/service.log"

sudo service rundeckd restart
# systemctl restart rundeckd
