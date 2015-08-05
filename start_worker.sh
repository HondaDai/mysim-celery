nohup celery \
  -A tasks worker \
  --loglevel=info \
  --concurrency=4 \
  --pidfile="$HOME/log/celery/%n.pid" \
  --logfile="$HOME/log/celery/%n.log" \
  -- celeryd.prefetch_multiplier=4 &
