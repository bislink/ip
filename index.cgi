#!/usr/bin/perl 

=head1 Provide IP for JavaScript
Usage: 
1. <script src="http://bislinks.com/git-repos/ip/index.cgi"></script> 
2. <script type="text/javascript">document.write('Your IP is ' + bl_user_ip+ ''); </script>
=cut

use CGI qw(:standard :escape :escapeHTML);
my $q = new CGI;
use strict;
use CGI::Carp qw/fatalsToBrowser/;

my $get_source = `cat $0`;

my $source;
		$source .= qq{
<ol>
<li>#!/usr/bin/perl</li>

<li>use CGI qw(:standard);</li>

<li>my \$ip = \$ENV{'REMOTE_ADDR'};</li>

<li>print header('text/javascript');</li>

<li>print qq{ var bl_user_ip = '&lt;a href="http://bislinks.com" title="Your IP is \$ip.  Powered by BISLINKS.com" style="text-decoration:none;"&gt;\$ip&lt;/a&gt;'; };</li>
</ol>
};

my $ip = $ENV{'REMOTE_ADDR'};

if (param) {
	my $qry_str = $ENV{'QUERY_STRING'};
	
	if ($qry_str eq 'source') {

		my $meta = qq{<meta charset="utf-8"/>};
		my $header = sprintf header();
		$header =~ s!charset=.*!charset=utf-8!;
		$header .= start_html(-title => "Source");
		$header =~ s{<!DOCTYPE.*>}{<!DOCTYPE html>}s;
		$header .= qq{<html>\n<head>\n<title>Source</title>\n$meta\n</head>\n<body>\n};
		
		
		print $header;
		#print qq{<textarea rows="15" cols="60">} . escapeHTML($get_source) . qq{</textarea>}, end_html();
		print $source, end_html();
	} elsif ( $qry_str eq 'ip') {
		print header(-type=>'text/javascript');
		print qq{var bl_user_ip = '<a href="http://$ip" title="Your IP is $ip. Powered by BISLINKS.com/free/ip" style="text-decoration:none;">$ip</a>'; };
	
	} elsif ($qry_str eq 'ajax') {
		print header(-type=>'text/html');
		print qq{$ip};
	} elsif ($qry_str eq 'xml') {
		my $out;
		for (keys %ENV) {
			next if $_ =~ /HTTP_COOKIE/;
			$out .= qq{<$_>$ENV{"$_"}</$_>} if $_;	#<environment>$out</environment>
		}
		print header(-type=>'application/xml');
		print qq{<?xml version="1.0" encoding="UTF-8"?>
<ip>
	<instructions>http://bislinks.com/free/ip/instructions.htm</instructions>
	<address>$ip</address>
</ip>
};
		
	} elsif ($qry_str eq 'json') {
		print header(-type=>'text/javascript');
		my $out = qq~{ "userIP": 
	[
		{"Instructions":"http://bislinks.com/free/ip/instructions.htm"},
		{"ViaAJAX":"http://bislinks.com/free/ip/index.cgi?ajax"},
		{"AsXML":"http://bislinks.com/free/ip/index.cgi?xml"},
		{"ViaJS":"http://bislinks.com/free/ip/index.cgi?js"},
		{"YourIP":"$ip"}
	]
}
~;

print qq~{
	"Instructions":"http://bislinks.com/free/ip/instructions.htm",
	"ViaAJAX":"http://bislinks.com/free/ip/index.cgi?ajax",
	"AsXML":"http://bislinks.com/free/ip/index.cgi?xml",
	"ViaJS":"http://bislinks.com/free/ip/index.cgi?js",
	"YourIP":"$ip"
}
~;

	}	# end json 

} else {
escapeHTML($source);
#print header('text/javascript');
print header('text/html');
#print qq{var bl_user_ip = '<a href="http://bislinks.com" title="Your IP is $ip.  Powered by BISLINKS.com" style="text-decoration:none;">$ip</a>'; document.write('<textarea rows="15" cols="60">$source</textarea>');};
print $source;

}
