#!/usr/bin/perl 

=head1 Provide IP for JavaScript
Usage: <script src="http://bislinks.com/git-repos/ip/index.cgi"></script>
=cut

use CGI qw(:standard :escape :escapeHTML);
use strict;
use CGI::Carp qw/fatalsToBrowser/;

my $ip = $ENV{'REMOTE_ADDR'};

print header('text/javascript');
print qq{ var bislinks_ip = "$ip"; };


