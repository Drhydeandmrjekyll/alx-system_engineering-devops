# 7-puppet_install_nginx_web_server.pp

# Define a class for Nginx installation and configuration
class nginx_server {
  # Install Nginx package
  package { 'nginx':
    ensure => 'installed',
  }

  # Ensure Nginx service is running and enabled
  service { 'nginx':
    ensure => 'running',
    enable => true,
  }

  # Configure Nginx to listen on port 80
  file { '/etc/nginx/sites-available/default':
    ensure  => 'file',
    content => template('nginx/default.conf.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  # Define custom template for Nginx configuration
  file { '/etc/nginx/sites-available/default.conf.erb':
    ensure  => 'file',
    source  => 'puppet:///modules/nginx/default.conf.erb',
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  # Ensure Nginx responds with "Hello World!" at root path
  file { '/var/www/html/index.html':
    ensure  => 'file',
    content => 'Hello World!',
    require => Package['nginx'],
    notify  => Service['nginx'],
  }
}

# Include Nginx class
include nginx_server

# Define redirect resource for /redirect_me
nginx::resource::location { 'redirect_me':
  location    => '~ ^/redirect_me',
  ensure      => 'present',
  vhost       => 'default',
  proxy       => 'http://example.com',
  ssl         => false,
  ssl_cert    => '',
  ssl_key     => '',
  ssl_port    => '',
  ssl_verify  => '',
  ssl_version => '',
  ssl_ciphers => '',
}
