import turtle
t = turtle.Turtle()

count =0
while count < 100 : 
    t.forward(50)  
    t.left(20)
    t.left(20 - count/100)
    t.left(165)
count = count + 1

input()
