# Puppet manifest to kill process named "killmenow" using pkill
exec { 'killmenow_process':
  command  => '/usr/bin/pkill killmenow',
  provider => 'shell',
  returns   => [0, 1],
}
