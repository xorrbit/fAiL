alphanum = ([*('a'..'z'),*('A'..'Z'),*('0'..'9')])

5000000.times { |pos|
  file = (0..5).map{ alphanum[rand(62)] }.join
  puts "hit: #{file} pos: #{pos}" if file.downcase.include? 'fail'
}

