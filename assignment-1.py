
"""
Question 1
"""
numberOfRows = 4 


print("a\t","a^3\t","a^4")

for i in range(numberOfRows):
    k = i+1
    l = k**3
    m = l*k
    numbers = [k,l,m]
    for j in numbers:
        print(j, end="\t")   
    
    print("\n")

"""
Question 2
"""
# There will be two counts, but I wrote it as it can be as wished

number_of_times = int(input("Enter how many times you would like to enter numbers: "))
step_counts = []

for i in range(number_of_times):
    n = int(input("Enter the step count: "))
    step_counts.append(n)

multiplication_number = 4
results = []
for i in range(len(step_counts)):
    result = 0
    for j in range(step_counts[i]):
        if j % 2 == 0:
            result += 1/((2*j)+1)
        else:
            result -= 1/((2*j)+1)
    result*=multiplication_number
    results.append(result)

for i in results:
    print(i, end="\n")


"""
Question 3
"""

number = int(input("Enter a six digit number: "))

# Check if the number is six digit

if len(str(number)) == 6:
    print(number%10)
    number //=10
    print(number%10)
    number //=10
    print(number%10)
    number //=10
    print(number%10)
    number //=10
    print(number%10)
    number //=10
    print(number%10)

"""
Question 4
"""   

#part a

uni_code = eval(input("Enter the code: "))
print("The character is: ", chr(uni_code))

#part b
import turtle as trt

trt.write("\uFE9D    \uFEB5   \u0394   \u03B4    \u03C6", font=('Times New Roman', 28, 'bold'))
trt.done()


"""
Question 5
"""
trt.penup()
trt.fillcolor("black")
trt.goto(0,-300)
trt.pendown()
trt.circle(300)
trt.penup()
trt.goto(-125,75)
trt.pendown()
trt.begin_fill()
trt.circle(60)
trt.end_fill()
trt.penup()
trt.goto(125,75)
trt.pendown()
trt.begin_fill()
trt.circle(60)
trt.end_fill()
trt.penup()
trt.goto(-80, 0)
trt.pendown()
trt.goto(0,100)
trt.goto(80, 0)
trt.penup()
trt.goto(-145, -50)
trt.pendown()
trt.goto(0, -150)
trt.goto(145, -50)
trt.penup()

trt.done()