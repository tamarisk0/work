import turtle
#设置背景色，填充色
turtle.bgcolor("red")
turtle.fillcolor("yellow")
turtle.color('yellow')
turtle.speed(5)
#最大的星星
turtle.begin_fill()
turtle.up()
turtle.goto(-600,220) 
turtle.down()
for i in range (5):    
    turtle.forward(150)
    turtle.right(144)
turtle.end_fill()

#第1颗小星星
turtle.begin_fill()
turtle.up()
turtle.goto(-400,295)
turtle.setheading(305)
turtle.down()
for i in range (5):    
    turtle.forward(50)
    turtle.left(144)

turtle.end_fill()


#第2颗小星星
turtle.begin_fill()
turtle.up()
turtle.goto(-350,212)
turtle.setheading(30)
turtle.down()
for i in range (5):  
    turtle.forward(50)
    turtle.right(144)

turtle.end_fill()

#第3颗小星星
turtle.begin_fill()
turtle.up()
turtle.goto(-350,145)
turtle.setheading(5)
turtle.down()
for i in range (5):   
    turtle.forward(50)
    turtle.right(144)

turtle.end_fill()

#第4颗小星星
turtle.begin_fill()
turtle.up()
turtle.goto(-400,90)
turtle.setheading(300)
turtle.down()
for i in range (5):  
    turtle.forward(50)
    turtle.left(144)

turtle.end_fill()

#武汉加油
turtle.penup()
turtle.goto(20,-30)
turtle.color("black")
turtle.write("武汉加油！\n中国加油！", font=('Arial', 80, 'normal'))

