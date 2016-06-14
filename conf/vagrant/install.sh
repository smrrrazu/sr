#!/usr/bin/env bash

# Fixing the locale/encoding environment
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

# Variables
DB_PWD=""

echo -e "\n--- Updating package list ---\n"
apt-get -qq update

echo -e "\n--- Installing Apache, MySQL and phpMyAdmin ---\n"
# Unattended install for MySQL
export DEBIAN_FRONTEND="noninteractive"
# Unattended install for phpMyAdmin
echo "phpmyadmin phpmyadmin/dbconfig-install boolean true" | debconf-set-selections
echo "phpmyadmin phpmyadmin/app-password-confirm password $DB_PWD" | debconf-set-selections
echo "phpmyadmin phpmyadmin/mysql/admin-pass password $DB_PWD" | debconf-set-selections
echo "phpmyadmin phpmyadmin/mysql/app-pass password $DB_PWD" | debconf-set-selections
echo "phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2" | debconf-set-selections
apt-get install -y apache2 mysql-server-5.6 phpmyadmin
php5enmod mcrypt

# If symlink does not exist, create a dir /var/www/domains/ and a symlink to /sr/ dir
if ! [ -L /var/www/domains/sr ]; then 
    mkdir -p /var/www/domains
    ln -s /vagrant /var/www/domains/sr
fi

# Fixes the error of importing HTTPSHandler when creating virtualenv
apt-get install -y libssl-dev

# Install pip for Python 3.x
apt-get install -y python3-pip
pip3 install --upgrade pip

# Install Invoke - Pythonic task execution tool
pip3 install invoke

# Open project directory
cd /vagrant

# Copy mysql config file
cp -n /var/www/domains/sr/conf/mysql/my.cnf /home/vagrant/.my.cnf
cp -n /var/www/domains/sr/conf/mysql/my.cnf /root/.my.cnf

# Create logs folder
mkdir -p /vagrant/sr/logs/

# # Create a symlink local settings to vagrant specific setting
# cd /vagrant/sr
# if ! [ -L local_settings.py ]; then
#     ln -s local_settings_vagrant.py local_settings.py
# fi
# cd /vagrant

# # Install project packages including virtual environment
# invoke install

# # Remove the default Apache config if it exists
# if [ -a /etc/apache2/sites-enabled/000-default.conf ]; then
#     rm /etc/apache2/sites-enabled/000-default.conf
# fi

# # Create a symlink of the apache config if it doesn't exist already
# if ! [ -L /etc/apache2/sites-enabled/sr-dev.conf ]; then
#     ln -s /var/www/domains/sr/conf/apache/sr-dev.conf /etc/apache2/sites-enabled/sr-dev.conf
# fi

service apache2 restart