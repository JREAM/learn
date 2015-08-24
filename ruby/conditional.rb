age = 25

if age > 50
  puts "You are over 50"
elsif age > 30
  puts "You are over 30"
elsif age > 20
  puts "You are over 20"
else
  puts "I dunno"
end

if age == 25
  puts "You are 25"
else
  puts "You are not 25"
end

unless age == 30 then
  print "Well this syntax is whack!"
end

really = true
puts "It is true!" unless really
puts "It is true!" if really

case age
when 0 .. 5
  puts "baby"
when 6 .. 12
  puts "child"
when 13 .. 17
  puts "teenager"
else
  puts "adult"
end
