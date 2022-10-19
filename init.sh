sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo gunicorn -w 2 -c /home/box/web/etc/hello.py hello:wsgi_application
sudo ln -sf /home/box/web/etc/qa.py /etc/gunicorn.d/qa.py
sudo gunicorn -w 2 -c /home/box/web/etc/qa.py ask.wsgi:application
sudo /etc/init.d/gunicorn restart
