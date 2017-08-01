#!/usr/bin/perl 

=head1 Provide IP for JavaScript
Usage: 
1. <script src="http://bislinks.com/free/ip/ip.cgi"></script> 
2. <script type="text/javascript">document.write('Your IP is ' + user_ip+ ''); </script>
=cut

use strict;
use warnings;

use vars qw($header $header_xml $header_js $header_json $ip $query_string $source $net_type);

$header = "Content-Type: text/html \n\n";
$header_json = "Content-Type: application/json\n\n";
$header_xml = "Content-Type: application/xml\n\n";
$header_js = "Content-Type: text/javascript\n\n";

$ip = $ENV{'REMOTE_ADDR'} || "";
$query_string = $ENV{'QUERY_STRING'} or "";
$source = qq{
<ol>
<li>#!/usr/bin/perl</li>
<li>use strict;</li>
<li>use warnings;</li>
<li>my \$ip = \$ENV{'REMOTE_ADDR'} or "";</li>
<li>print "Content-type: text/javascript \n\n</li>
<li>print qq{ var user_ip = "\$ip"};</li>
</ol>
};

	if ($query_string eq 'source') {
		print $header, $source;
		
	} elsif ( $query_string eq 'js') {
		print $header_js, qq{/* JavaScript */\n var user_ip = "$ip";}; 
	
	} elsif ($query_string eq 'ajax') {
		print $header;
		print qq{$ip};
		
	} elsif ($query_string eq 'xml') {
		print $header_xml;
		print qq{<?xml version="1.0" encoding="UTF-8"?>
<ip>
	<instructions>https://bislinks.com/free/ip/instructions.htm</instructions>
	<address>$ip</address>
</ip>
};
		
	} elsif ($query_string eq 'json') {

# prepare json		
		my $out = qq~{ "userIP": 
	[
		{"Instructions":"https://bislinks.com/free/ip/instructions.htm"},
		{"ViaAJAX":"https://bislinks.com/free/ip/index.cgi?ajax"},
		{"AsXML":"https://bislinks.com/free/ip/index.cgi?xml"},
		{"ViaJS":"https://bislinks.com/free/ip/index.cgi?js"},
		{"YourIP":"$ip"}
	]
}
~;

# to browser
print $header_json;
print qq~{
	"Instructions":"https://bislinks.com/free/ip/instructions.htm",
	"ViaAJAX":"https://bislinks.com/free/ip/index.cgi?ajax",
	"AsXML":"https://bislinks.com/free/ip/index.cgi?xml",
	"ViaJS":"https://bislinks.com/free/ip/index.cgi?js",
	"YourIP":"$ip"
}
~;

	}	# end json 

else {
print $header, 
qq{<!doctype html>
<html>
<head>
<title>IP</title>
<script src="./ip.cgi?js"></script>
</head>
<body>
	<h1>IP</h1>
	
	<nav>
		<ul>
			<li><a href="?xml">XML</a></li>
			<li><a href="?js">JavaScript</a></li>
			<li><a href="?json">jSON</a></li>
		</ul>
	</nav>
	
	<main id="main" class="container"><h2>Your IP</h2>
		<script> document.write(user_ip); </script>

		<h3>Instructions</h3>
		<div>
			<h4>Embed Perl/JavaScript in HTML</h4>
			<pre><code>&lt;script src="./ip.cgi?js">&lt;/script&gt;</code></pre>
		</div>
		<div>
			<h4>Call JavaScript</h4>
			<pre><code>&lt;script&gt;document.write( user_ip );&lt;/script&gt;</code></pre>
		</div>
	</main>

</body>
</html>
};

}
