python manage.py runserver 8080 #默认使用8000端口
#python manage.py runserver 8080 #指定启动端口
#python manage.py runserver 127.0.0.1:9000 #指定IP和端口
#pip freeze > requirements.txt
#pip install -r requirements.txt
#pip3.10 install Django==4.0.5
#systemctl start  mysqld
#systemctl status  mysqld
#alter user root@localhost  identified by 'jia844810';
#grant all privileges on *.*  to root@localhost  identified by 'Jia@844810';
#grant all privileges on *.*  to root@'%'  identified by 'Jia@844810';
#python manage.py dumpdata > data.json
#ps -ef|grep uwsgi
#uwsgi  --ini  uwsgi.ini
#uwsgi --stop uwsgi.pid
#uwsgi --reload uwsgi.pid
#./nginx -s reload
#python manage.py collectstatic
#python manage.py loaddata data1.json
# netstat -ntlp
# 多窗口tmux
#现在按下你 Tmux 的 PREFIX 键（默认是 Ctrl+B），再按 d 从 Tmux 中脱离出来，这样即使 ssh 断开连接了也能保持后台运行，想查错也可以用
#goaccess  -f /usr/local/nginx/logs/access.log -a > /usr/local/nginx/html/stat/index.html

#python manage.py migrate --fake sites zero
#python manage.py showmigrations
#python manage.py migrate sites