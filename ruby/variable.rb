$global_var = "everywhere"

def inside_method()
  puts "Hey #$global_var"
end

inside_method()
