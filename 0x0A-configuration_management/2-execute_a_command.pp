# Define the Puppet manifest to kill the process
class kill_process {
    exec { 'killmenow':
        command     => '/usr/bin/pkill -f killmenow',
        path        => '/usr/bin',
        refreshonly => true,
    }
}

# Apply the class
include kill_process

