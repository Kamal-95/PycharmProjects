str = "kamalKumar.com.commmmm"
str2 = "RahulSharma.com"
str3 = "Kumar"
print(str[1])
print(str[3:7])    # substring in python

print(str + str2)  #concatenation

print(str3 in str) # substring check

var = str.split(".")
print(var)
print(var[1])

str4 = "    kamala pasand    "
print(str4.strip())  # both side strip
print(str4)

print(str4.lstrip())  # left side strip
print(str4.rstrip())  # right side strip