#!/usr/bin/env bash
# Using puppet connecting without password

file { '/etc/ssh/ssh config':
  ensure => present,
}

file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PaaswordAuthentication no',
  match   => '^#PasswordAuthentication',
}

file_line { 'Declare identity file':
  path    => '/etc/ssh_config',
  line    => 'IdentityFile  ~/.ssh/school',
  match   => '^#identityFile',
}
