import multiprocessing

bind = "0.0.0.0:8000"
#workers = multiprocessing.cpu_count() * 2 + 1
workers = 1
threads = 3
accesslog = "-"
errorlog = "-"
forwarded_allow_ips = "*"
proxy_allow_ips = "*"
pythonpath='/app/website'
