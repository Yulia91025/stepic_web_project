sudo pip3 install --upgrade django
git clone https://github.com/Yulia91025/stepik_web_project web
sudo /etc/init.d/mysql start
mysql -uroot -e "create database web;"
mysql -uroot -e "create user 'box'@'localhost' identified by '12345';"
mysql -uroot -e "grant all privileges on web.* to 'box'@'localhost' with grant option;"
cd ~/web/ask
python3 manage.py makemigrations qa
python3 manage.py migrate
cd ~/web
bash init.sh
