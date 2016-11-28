#!/usr/bin/perl

use strict;
use warnings;
use FindBin;
use lib "$FindBin::Bin/lib/", "$FindBin::Bin/local/lib/perl5";
use Grid::HTML5;

my $imgpath = "./data/img/";
my $txtpath = "./data/text/";

my $numfiles = 0;
opendir(my $dh, $imgpath);
while (my $de = readdir($dh)) {
      next if $de =~ /^\./ or $de =~ /config_file/;
      $numfiles++;
}
closedir($dh);

## needs to grep all imgs and txts

##reverse sorted to highest number is last.


Grid::HTML5::begin_html("Grid");
Grid::HTML5::generate_header();

## outputs to screen.
print <<EOT;

<br>
<b> There are $numfiles posts so far </b> <br><br>
<br>
EOT

my $count = $numfiles;

while($count != 0) {

	my $thisfile = $txtpath . $count . ".txt";

	my $img = $imgpath . $count . ".jpg";

	my($file);
	undef $/;
	open (FH, $thisfile);
	$file= <FH>;
	close(FH);

	$file =~ s#\n#<br>\n#g;

	print "<div style='border:1px #000 solid; padding:5px; width:550px;'>\n";
	print $file;

	print "<br><a href=\"" . $img . "\">";

	print "<img src=\"" . $img . "\" width ='100'></a>\n";

	print "</div><br>";

	$count--;
}

print "</div><br>";

Grid::HTML5::generate_footer();
Grid::HTML5::end_html();
