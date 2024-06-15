# Puppet manifest to adjust the file descriptor limit for the holberton user

exec { 'change-os-configuration-for-holberton-user':
  command     => 'sudo su -c "echo \"holberton hard nofile 4096\" >> /etc/security/limits.conf"',
  path        => '/bin:/usr/bin:/sbin:/usr/sbin',
  refreshonly => true,
}

exec { 'reload-limits':
  command     => 'sudo sysctl -p',
  path        => '/bin:/usr/bin:/sbin:/usr/sbin',
  refreshonly => true,
}
