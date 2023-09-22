# Puppet manifest to kill process named "killmenow" using pkill
exec { 'kill_killmenow_process':
  command     => 'pkill killmenow',
  onlyif      => 'pgrep killmenow',
  refreshonly => true,
  subscribe   => File['/path/to/your/killmenow_script'],
}
