# Fixing Nginx to handle high number of requests

exec { 'fix--for-nginx':
  command => 'sed -i "s/worker_connections  768;/worker_connections  2048;/" /etc/nginx/nginx.conf',
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Exec['fix--for-nginx'],
}
