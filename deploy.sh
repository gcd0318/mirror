rm -f /etc/mirror
mkdir /etc/mirror
cp -r conf/* /etc/mirror

mkdir /var/log/mirror

cp mirror.service /usr/lib/systemd/system
systemctl reenable mirror
systemctl restart mirror.service
