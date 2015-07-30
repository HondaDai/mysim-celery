celery multi start \
  -A tasks worker \
  --loglevel=info \
  --concurrency=1 \
  --logfile="$HOME/log/celery/%n.log" \
  -- celeryd.prefetch_multiplier=1 