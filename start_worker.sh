celery \
  -A tasks worker \
  --loglevel=info \
  --concurrency=1 \
  --pidfile="$HOME/log/celery/%n.pid" \
  --logfile="$HOME/log/celery/%n.log" \
  -- celeryd.prefetch_multiplier=1 

# usage: nohup sh start_worker.sh