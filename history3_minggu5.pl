#!/usr/bin/perl
use POSIX;

sub rek {
	$mid = floor(($up - $lo ) / 2 + $lo ) ;
	if($lo >= $up || $up <= $lo ) {
		return -1 ;
	}
	elsif($n == $arr[$mid]) {
		  return $mid ;
	}
	elsif($n > $num[$mid]) {
		$lo = $mid + 1 ;
	}
	else{
  		$up = $mid - 1 ;
	}
	rek($lo , $up , $n , @arr );
}

sub main
{
	@arr = (1,2,3,4,5);
	print"Masukkan input: ";
	chomp($n = <STDIN>);
	$lo = 0;
	$up = scalar @arr ;
	$hasil = rek($lo , $up , $n , @arr);
	if($hasil == -1)
	{
		print "Angka tidak dapat ditemukkan \n" ;
	}
	else 
	{
		print "Angka $n ada di index $hasil \n" ;
	}
}

main();
