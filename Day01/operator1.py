num1 = float(input("enter first number:"))
num2 = float(input("enter Second number:"))

print ("sum:" , num1+ num2 )
print ("sub:" , num1 - num2 )
print ("multiplication:" , num1 * num2 )

if num2!= 0:
    print("div:", num1 / num2)
else:
    print("division is not possible")



#Comments
'''
num1 = 10, num2 = 0
10 / 0 → ❌ not possible

num1 = 0, num2 = 5
0 / 5 → ✅ = 0.0

Top number (num1) = can be 0 (no issue).

Bottom number (num2) = cannot be 0.'''


#output
'''
enter first number:2
enter Second number:8
sum: 10.0
sub: -6.0
multiplication: 16.0
div: 0.25

if num2 is 0 :
  enter first number:5
enter Second number:0
sum: 5.0
sub: 5.0
multiplication: 0.0
division is not possible  '''