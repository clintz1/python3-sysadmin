# Setting up PostgreSQL Lab Server
#!/bin/sh

# Setting up PostgreSQL Lab Server
curl -o db_setup.sh https://raw.githubusercontent.com/linuxacademy/content-python3-sysadmin/master/helpers/db_setup.sh
chmod +x db_setup.sh
./db_setup.sh

# Installing The Postgres 9.6 Client
wget https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
yum install -y pgdg-redhat-repo-latest.noarch.rpm
yum update -y
yum autoremove -y postgresql
yum install -y postgresql96
apt-get install postgres-client-9.6

# Test connection from Workstation
psql postgres://[USERNAME]:[PASSWORD]@[SERVER_IP]:80/sample -c "SELECT count(id) FROM employees;"
