# Puppet manifest to kill a process named "killmenow" using pkill
exec { 'killmenow':
  command     => '/usr/bin/pkill killmenow',
  refreshonly => true,
  subscribe   => Exec['start_killmenow'],
  returns     => [0, 1],
}

exec { 'start_killmenow':
  command     => '/usr/bin/pkill killmenow',
  user        => 'shell',            
  logoutput   => true,    
  refreshonly => true,
  notify      => Exec['killmenow'],    
}
