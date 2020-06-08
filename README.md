* 钉钉接口说明
 [自定义机器人开发](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq)
 
* 参考

[python之钉钉机器人zabbix报警](https://blog.51cto.com/m51cto/2051945)

* 代码部署

1. 安装python

```
wget https://www.python.org/ftp/python/3.6.10/Python-3.6.10.tgz
tar -zxvf Python-3.6.10.tgz
mkdir /usr/local/python3
yum install gcc
Python-3.6.10/configure --prefix=/usr/local/python3/
make
make install
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```

2. 同步代码

`
scp -r ~/Documents/workspace/python/notification root@172.16.245.249:/home/jianzhang/notification
`

3. 安装依赖

`
pip install -r requirements.txt
`

4. 定时

`crontab -e`
```
30 18 * * 5 /usr/bin/python3 /home/jianzhang/notification/NotificationWeeklyReports.py 2>&1
* * * * * python安装路径 运行文件路径
│ │ │ │  │
│ │ │ │  └─── 星期几 (0 - 6) (0到6 0代表周日 1周一)
│ │ │ └──────── 月份 (1 - 12)
│ │ └───────────── 每月几号 (1 - 31)
│ └────────────────── 小时 (0 - 23)
└─────────────────────── 分钟 (0 - 59)
```