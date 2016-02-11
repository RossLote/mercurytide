import multiprocessing

command = '../env/bin/gunicorn'
pythonpath = '../'
bind = '127.0.0.1:8080'
workers = (multiprocessing.cpu_count() * 2) + 1
user = 'ross'
timeout = 300
