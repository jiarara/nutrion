#https://easyengine.io/tutorials/nginx/log-parsing/
#https://shaohualee.com/article/691
#$remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent"
# UV  ip
awk '{print $1}'  access.log  | sort  |uniq -c  | wc -l
# 所有的 pv
awk '{print $7 }' access.log |wc -l
# 访问最多的页面
awk '{print $7 }' access.log  | sort | uniq -c | sort -n -k 1 -r | more
# 访问最多的ip
awk '{print $1 }' access.log  | sort | uniq -c | sort -n -k 1 -r | more
# 访问最多的ip  前10
awk '{print $1 }' access.log  | sort | uniq -c | sort -n -k 1 -r | head -n 10

awk '{print $6}' /usr/local/nginx/logs/access.log | sort | uniq -c | sort -nr -k1 | head -n 1
# 统计当天pv
grep "16/Jul/2022" /usr/local/nginx/logs/access.log | wc -l

grep "16/Jul/2022"  | awk '{print $1}' /usr/local/nginx/logs/access.log | sort -n | uniq | wc -l
