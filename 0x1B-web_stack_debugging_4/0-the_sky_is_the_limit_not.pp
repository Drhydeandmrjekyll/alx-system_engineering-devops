# Increase amount of traffic Nginx server can handle

# Increase ULIMIT of default file.
exec { 'fix-for-nginx':
    # Modify ULIMIT value
    command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
    # Specify path for sed command
    path    => '/usr/local/bin/:/bin/',
}

# Restart Nginx
exec { 'nginx-restart':
    # Restart Nginx service
    command => '/etc/init.d/nginx restart',
    # Specify path for the init.d script
    path    => '/etc/init.d/',
}
