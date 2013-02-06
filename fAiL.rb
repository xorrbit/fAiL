5000000.times { |pos|
  file = (0..5).map{ ([*('a'..'z'),*('A'..'Z'),*('0'..'9')])[rand(62)] }.join
  puts "hit: #{file} pos: #{pos}" if file.downcase.include? 'fail'
}

