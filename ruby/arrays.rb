ppl = Array.new(10)
puts ppl.size
puts ppl.length

ppl = Array.new(2, "fred")
puts "#{ppl}"

# Some crazy stuff
num = Array.new(20) { |i| i = i + 1 }
puts "#{num}"

digits = Array(0..9)
puts "#{digits}"

static = []
django = []

static.push(["firetv"])
django.push(*[
    'admin',
    'test0', 'test1', 'test2', 'test3', 'test4',
    'test5', 'test6', 'test7', 'test8', 'test9',
])

print static
print django

