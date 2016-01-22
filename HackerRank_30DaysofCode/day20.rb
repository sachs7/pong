sentence = gets.chomp
result = sentence.scan(/[A-Z]+/i)
puts result.size
puts result
