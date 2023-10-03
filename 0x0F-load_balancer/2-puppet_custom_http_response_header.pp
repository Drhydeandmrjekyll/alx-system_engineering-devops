#!/usr/bin/env bash
## Installs Nginx with puppet with following configurations:
#+    Listens on port 80.
#+    Returns page containing "Hello World!" when queried
#+     at the root with a curl GET request.
#+    Configures /redirect_me as a "301 Moved Permanently".
#+    Includes a custom 404 page containing "Ceci n'est pas une page".
#+    Contains a custom HTTP header named X-Served-By.
#+    Value of HTTP header is hostname of running server.
# Install the puppetlabs-apt module to manage APT repositories
# Combined Puppet Manifest

# Define a custom fact to retrieve the hostname of the server
Facter.add('server_hostname') do
  setcode 'hostname'
end

# Install the puppetlabs-apt module to manage APT repositories
class { 'apt':
  update => {
    frequency => 'daily',
  },
  purge_sources_list.d => true,
}

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Create a custom template for the Nginx configuration
file { '/etc/nginx/default.erb':
  ensure  => 'file',
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Create a template for the Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure => 'file',
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Create the custom HTTP response header in Nginx configuration
file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => 'file',
  content => "add_header X-Served-By $::server_hostname;\n",
  notify  => Service['nginx'],
}

# Create the Nginx default site configuration
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => '
    server {
      listen 80 default_server;
      listen [::]:80 default_server;
      add_header X-Served-By $::server_hostname;
      root /var/www/html;
      index index.html index.htm;

      location /redirect_me {
        return 301 https://youtube.com/;
      }

      error_page 404 /404.html;
      location /404 {
        root /var/www/html;
        internal;
      }
    }
  ',
  notify  => Service['nginx'],
}
# Ensure the Nginx service is running and enabled
service { 'nginx':
  ensure  => 'running',
  enable  => true,
}
