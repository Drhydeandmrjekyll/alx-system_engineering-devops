exec { 'killmenow':
  command     => '/usr/bin/pkill killmenow',
  onlyif      => 'pgrep killmenow',
  provider    => 'shell',
  refreshonly => true,
  returns     => [0, 1],
}
