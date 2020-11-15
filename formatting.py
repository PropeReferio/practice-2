name = 'Bo'
name2 = 'John'

print('I want to go to %s\'s house' %name)
print('I want to go to %s\'s house and see %s' %(name, name2))

# %d for integers, %f for floating-point values, %b for binary format
dogs = 56
print('There are %d dogs at %s\'s house' %(dogs, name))


# Rounding / trailing decimal places
print('The value of pi is: %1.4f' %(3.141592))
print('The value of pi is: %1.6f' %(3.141592))
print('The value of boof is: %4.8f' %(3.0))



print('{2} {1} {0}'.format('directions', 
                           'the', 'Read'))


print('a: {a}, b: {b}, c: {c}'.format(a = 1, 
                                      b = 'Two', 
                                      c = 12.3))

# They can be reused:

print('The first {p} was alright, but the {p} {p} was tough.'.format(p = 'second'))

#f strings:

a = 5
  
b = 10
  
print(f"He said his age is {2 * (a + b)}.") 


# Float precision in the f-String method:

#     Syntax: {value:{width}.{precision}}


num = 3.14159
  
print(f"The value of pi is: {num:{1}.{5}}")

# f-strings are faster and better than both %-formatting and str.format(). 
# f-strings expressions are evaluated are at runtime, and we can also embed 
# expressions inside f-string, using a very simple and easy syntax. The 
# expressions inside the braces are evaluated in runtime and then put together
#  with the string part of the f-string and then the final string is returned.
