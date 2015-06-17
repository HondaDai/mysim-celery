import os
import time
import random
import socket
from celery import Celery


# BROKER_URL = ""
# CELERYD_MAX_TASKS_PER_CHILD = 1

CELERY_ACKS_LATE = True
CELERYD_PREFETCH_MULTIPLIER = 1

if socket.gethostname() == 'HsM.local':
  ns_path = "/Volumes/Transcend/ns-allinone-3.23/ns-3.23"
else:
  ns_path = "~/ns-allinone-3.23/ns-3.23"

os.chdir(ns_path)

def build_mysim(mysim_param):
  return "./waf --run \"scratch/mysim/mysim %s\"" % (mysim_param)

app = Celery('tasks', backend='redis', broker='redis://localhost:6379/0')

@app.task
def add(x, y):
  print "start!"
  time.sleep(10)
  return x + y

@app.task
def run_simulation(params):
  # time.sleep(random.randint(0,5))
  cmd = "%s" % (build_mysim(params))
  # print cmd
  os.system(cmd)
  return cmd




