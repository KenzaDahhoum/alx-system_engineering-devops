# 0-strace_is_your_friend.pp
# This Puppet manifest fixes all instances of "phpp" to "php" in the wp-settings.php file.

exec { 'fix_phpp':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
  onlyif  => 'grep -q phpp /var/www/html/wp-settings.php',  # This ensures the command runs only if "phpp" is found
}

service { 'apache2':
  ensure  => running,
  enable  => true,
  subscribe => Exec['fix_phpp'],  # Restart Apache if the exec resource changes the file
}
