<?php

$characters = array('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9');

$iterations = 5000000;
$length = 6;

for($pos = 0; $pos < $iterations; ++$pos) {

	$file = "";

	foreach(array_rand($characters, $length) as $key) {
		$file .= $characters[$key];
	}

	if(preg_match("/fail/", strtolower($file))) {
		echo sprintf("hit: %s pos: %s\n", $file, $pos);
	}

}