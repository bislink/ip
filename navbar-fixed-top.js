//<!-- no jq methods 

function fixed_top_navbar(serverName, pageName, menuName, dropDownLinks, searchUrl) {

// usage: fixed_top_navbar('', '', 'Menu', 'm-=-mobile', 'google');
// First two will be filled in automatically by serverName and pageName respectively (localhost, first item after the first /)
	
	// serverName
	if ( serverName === undefined || serverName === '' ) {
		serverName = window.location.hostname;
	} else {
		serverName = serverName;
	}
	// pageName
	
	//A var to hold the corresponding link/url
	var pageLink = '';

	if ( pageName === undefined || pageName === '' ) {
	
		var path = window.location.pathname;
		var paths = path.split('/');
		
		if ( paths[1] === 'cgi-bin') {
			pageName = paths[2];
			pageLink += 'cgi-bin/' + paths[2];
		} else if ( paths[1] === '' ) {
			
			pageName = 'Home';		// Wed Feb  4 22:27:44 2015
			
		} else {
			pageName = paths[1];
			pageLink += paths[1];
		}
	} else {
		pageName = pageName;
	}
	
	// dropdownLinks
	
	var ddl = '';
	
	if (dropDownLinks === undefined || dropDownLinks === '') {
		//No additional links
		ddl += '';
		
	} else if ( dropDownLinks.match(/-=-/) ) {
	
		L  = dropDownLinks.split('-=-');

		for ( i=0; i<L.length; i++) {
			ddl += '<li><a href="/' + L[i] + '">' +L[i]+ '</a></li>';
		}
	}
	
	// Search URL
	var searchHTML = '';
	var searchID = '';
	var searchGoogleJS = '';
	//
	
	if ( searchUrl === undefined || searchUrl === '' ) {
	
		if ( serverName === 'localhost' ) {
			searchUrl = '//bislinks.com/cgi-bin/search/search.pl'; 
		} else {
			searchUrl = '/cgi-bin/search/search.pl';
		}
		
		searchHTML = '';
		
	} else if ( searchUrl === 'google' ) {
	
		searchUrl = 'http://search.bislinks.com/cgi-bin/index.cgi';
		
		searchID = 'id="cse-search-box"';
			
		searchHTML += '<div>';
		searchHTML += '<input type="hidden" name="cx" value="partner-pub-8434162582137179:8779217371" />';
		searchHTML += '<input type="hidden" name="cof" value="FORID:10" />';
		searchHTML += '<input type="hidden" name="ie" value="UTF-8" />';
		//searchHTML += '<input type="hidden" name="q" />';
		searchHTML += '<input type="hidden" name="sa" value="Search" />';
		searchHTML += '</div>';
		
		searchGoogleJS = '<script type="text/javascript" src="http://www.google.com/coop/cse/brand?form=cse-search-box&amp;lang=en"></script>';
		// The CSS it loads sure does change the look of the button!
		  
	} else {
	
		searchUrl = searchUrl;
		searchHTML = '';
		searchID = '';
		searchGoogleJS = '';
	}
	
	
	
	
	
var out = '';

out += '<nav class="navbar navbar-default navbar-fixed-top" role="navigation">';
out += '<div class="container" id="topNavBar">';
out += '<div class="navbar-header">';
out += '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">';
out += '<span class="sr-only">Toggle navigation</span>';
out += '<span class="icon-bar"></span>';
out += '<span class="icon-bar"></span>';
out += '<span class="icon-bar"></span>';
out += '</button>';
out += '<a class="navbar-brand" href="/">' +serverName+ '</a>';
out += '</div>';
out += '<div id="navbar" class="navbar-collapse collapse">';
out += '<ul class="nav navbar-nav">';
out += '<li class="active"><a href="/' +pageLink+ '">' +pageName+ '</a></li>';
out += '<li class="dropdown">';
out += '<a href="#" class="dropdown-toggle" data-toggle="dropdown">' +menuName+ '<span class="caret"></span></a>';
out += '<ul class="dropdown-menu" role="menu" id="DDUL">';
out += '<li><a href="/contact/">Contact</a></li>';
out += '<li><a href="/advertise/">Advertise</a></li>';
out += '<li class="divider"></li>';
out += '<li class="dropdown-header">BISLINKS</li>';
out += '<li><a href="http://bislinks.com/">Home</a></li>';
out += '<li><a href="http://bislinks.com/blog">blog</a></li>';
out += '<li><a href="http://bislinks.com/contact/">Contact</a></li>';
out += '<li><a href="http://bislinks.com/advertise">Advertise</a></li>';

out += ddl;

out += '</ul>';
out += '</li>';
out += '</ul>';
out += ' <ul class="nav navbar-nav navbar-right">';
out += '<li><a href="/about">About</a></li>';
out += '</ul>';
// SEARCH FORM
out += '<form class="navbar-form navbar-right" role="search" action="' +searchUrl+ '" method="get"' +searchID+ '>';
out += '' +searchHTML+ '';
out += '<div class="form-group">';
out += '<input type="text" name="Terms" class="form-control" placeholder="Search">';
out += '</div>';
out += '<button type="submit" class="btn btn-default glyphicon glyphicon-search" name="q" id="q"></button>';
out += '</form>';
out += '' +searchGoogleJS+ '';

out += '</div><!--/.nav-collapse -->';
out += '</div>';
out += '</nav>';

document.write (out) ;

}

//-->