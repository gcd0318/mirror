rm -f /etc/mirror
mkdir /etc/mirror
cp -r conf/* /etc/mirror

cp index.mirror.html /var/www/html

mkdir /var/log/mirror

cp -r autostart ~/.config

cp mirror.service /usr/lib/systemd/system
systemctl reenable mirror
systemctl restart mirror.service
