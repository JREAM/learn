i = 0
num = 20

while i < num do
  puts "we are at #{i}"
  i += 1
end

i = 0 # Reset
begin 
  puts "We are at #{i}"
  i += 1
end while i < num

i = 0
until i > num do
   puts "Until loop #{i}"
   i += 1
end

i = 0
begin
  puts "End until loop #{i}"
  i += 1
end until i > num

for j in 0..7
  puts "Count is at #{j}"
end

(0..5).each do |x|
  puts "Range each do at #{x}"
end

x = []
[].each do |x|
  puts "Range each do at #{x}"
end
