import turtle
from turtle import *
from time import sleep
from random import randint

winner_message_position = (-270, -300)
turtle_1_race = turtle_2_race = turtle_3_race = turtle_4_race = 0
finish_race = 490

def start_racing():
    for x in range(3):
        turtle.setposition(0, 0)
        turtle.write(3 - x, font=('Arial', 60, 'bold'))
        sleep(1)
        turtle.setposition(winner_message_position)
        turtle.clear()
        
    turtle.setposition(-125, 0)
    turtle.write('Ready?', font=('Arial', 60, 'bold'))
    sleep(1)
    turtle.clear()

def turtle_race():
    global turtle_1_race, turtle_2_race, turtle_3_race, turtle_4_race
    
    # Create the window
    window = turtle.Screen()
    window.title('Turtle Racing Occuring in this pop-up Window')
    turtle.bgcolor('Green')
    turtle.color('White')
    turtle.speed(0)
    turtle.penup()
    
    # Start de counting
    start_racing()
    
    turtle.setposition(-420, 260)
    turtle.write('Come one, Come All! It is Turtle Racing Time!', font=('Arial', 30, 'bold'))
    turtle.penup()
    
    # Setting up the dirt
    turtle.setposition(-280, 225)
    turtle.color('Brown')
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(520)
    turtle.right(90)
    turtle.forward(445)
    turtle.right(90)
    turtle.forward(520)
    turtle.right(90)
    turtle.forward(445)
    turtle.right(90)
    turtle.end_fill()
    
    # Making the finish line
    stamp_size = 20
    square_size = 15.5
    finish_line = 180
    
    turtle.color('White')
    turtle.shape('square')
    turtle.shapesize(square_size / stamp_size)
    turtle.penup()
    
    for i in range(14):
        turtle.setpos(finish_line, (211 - (i * square_size * 2)))
        turtle.stamp()
        
    for j in range(14):
        turtle.setpos(finish_line + square_size, ((211 - square_size) - (j * square_size * 2)))
        turtle.stamp()
    
    # Turtle Stat Blocks
    turtle_1 = Turtle()
    turtle_1.speed(0)
    turtle_1.color('Black')
    turtle_1.shape('turtle')
    turtle_1.penup()
    turtle_1.goto(-275, 140)
    turtle_1.pendown()

    turtle_2 = Turtle()
    turtle_2.speed(0)
    turtle_2.color('Yellow')
    turtle_2.shape('turtle')
    turtle_2.penup()
    turtle_2.goto(-275, 60)
    turtle_2.pendown()

    turtle_3 = Turtle()
    turtle_3.speed(0)
    turtle_3.color('LightBlue')
    turtle_3.shape('turtle')
    turtle_3.penup()
    turtle_3.goto(-275, -20)
    turtle_3.pendown()

    turtle_4 = Turtle()
    turtle_4.speed(0)
    turtle_4.color('Orange')
    turtle_4.shape('turtle')
    turtle_4.penup()
    turtle_4.goto(-275, -110)
    turtle_4.pendown()    
    
    # Final Loop   
    
    while True:
        turtle_1_speed = randint(1, 5)
        turtle_1_race += turtle_1_speed
        turtle_1.forward(turtle_1_speed)
        
        turtle_2_speed = randint(1, 5)
        turtle_2_race += turtle_2_speed
        turtle_2.forward(turtle_2_speed)
        
        turtle_3_speed = randint(1, 5)
        turtle_3_race += turtle_3_speed
        turtle_3.forward(turtle_3_speed)
        
        
        turtle_4_speed = randint(1, 5)
        turtle_4_race += turtle_4_speed
        turtle_4.forward(turtle_4_speed)
        
        if turtle_1_race >= finish_race:
            print(turtle_1_race)
            turtle.setposition(winner_message_position)
            turtle.write('Black Turtle is the winner!', font=('Arial', 30, 'bold'))
            break
        elif turtle_2_race >= finish_race:
            print(turtle_2_race)
            turtle.setposition(winner_message_position)
            turtle.write('Yellow Turtle is the winner!', font=('Arial', 30, 'bold'))
            break
        elif turtle_3_race >= finish_race:
            print(turtle_3_race)
            turtle.setposition(winner_message_position)
            turtle.write('Light Blue Turtle is the winner!', font=('Arial', 30, 'bold'))
            break
        elif turtle_4_race >= finish_race:
            print(turtle_4_race)
            turtle.setposition(winner_message_position)
            turtle.write('Orange Turtle is the winner!', font=('Arial', 30, 'bold'))
            break
        
    turtle.exitonclick()
    
while True:
    #draw_circle()
    #draw_octagon()
    #draw_triangle()
    #draw_square()
    #draw_star()
    #sleep(1)
    turtle_race()
    done()