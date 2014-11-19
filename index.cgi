#!/usr/bin/perl
# Load CGI library
use CGI qw( :standard );
# Get IP address 
my $ip = $ENV{'REMOTE_ADDR'};
# Print proper headers: Javascript, in this case
print header('text/javascript');
# Output as a Javascript variable!
print qq{ var get_user_ip = '<a href="http://bislinks.com" title="Your IP is $ip. Powered by BISLINKS.com">$ip</a>'; };
