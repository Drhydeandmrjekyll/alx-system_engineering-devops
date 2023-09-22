# Puppet manifest to kill a process named "killmenow" using pkill
exec { 'killmenow':
  command  => '/usr/bin/pkill killmenow',
  provider => 'shell',
  refreshonly => true,
  returns  => [0, 1],
}

