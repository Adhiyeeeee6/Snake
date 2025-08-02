import turtle
import time
import random

delay = 0.1 

#Score
score = 0
high_score = 0

#creating Screen to play

win = turtle.Screen() #creating screen to play game
win.title = ("The Snake Game") #title of game
win.bgcolor("green") #background color of screen
win.setup(width = 600.0 , height = 600.0) #screen setup pixels
win.tracer(0) #turns of the screen updates

#Snakehead

head = turtle.Turtle() #create entity
head.speed(0) #animation speed of turtle module
head.shape("square")
head.color("black")
head.penup() #to not draw line when it moves
head.goto(0,0) #center of screen start
head.direction = "stop" #to not move when run code

# Food

food = turtle.Turtle() 
food.speed(0) 
food.shape("circle")
food.color("red")
food.penup() 
x_food = random.randint(-290 , 290)
y_food = random.randint(-290 , 290)
food.goto(x_food , y_food)

#list to store snake segments

l = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score : 0 High Score : 0", align = "center" , font = ("Courier" , 24 , "normal"))


#Functions

def go_up():
    if head.direction != "down": #to not let snake go in reverse direction into its body
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20) 

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#keybord Bindings

win.listen() #to let window take command from keyboard
win.onkeypress(go_up , "w") #go up
win.onkeypress(go_down , "s") #go down
win.onkeypress(go_left , "a") #go left
win.onkeypress(go_right , "d") #go right


#Main game loop

while True:

    win.update()

    #check for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1) #to pause for 1 sec
        head.goto(0,0) # go to center
        head.direction = "stop"

        #Hide the body
        for i in l:
            i.goto(1000,1000)

        #clear the segments
        l.clear()

        #reset the score
        score = 0

        #reset the delay
        delay = 0.1

        pen.clear() #so it dosent overwrite
        pen.write("Score : {} High Score : {}".format(score,high_score), align = "center" , font = ("Courier" , 24 , "normal"))



    if head.distance(food) < 20: #if the snake reaches near food then food goes to another random spot
        #move food to random spot
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #add a segment to body after collision

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        new_segment.goto(1000,1000)
        l.append(new_segment)

        #Shorten the delay cuz of turtle module
        delay -= 0.001


        #increase the score after collision with food
        score += 10

        if score > high_score:
            high_score = score

        pen.clear() #so it dosent overwrite
        pen.write("Score : {} High Score : {}".format(score,high_score), align = "center" , font = ("Courier" , 24 , "normal"))


    #to make each new segments follow each other 
    for i in range(len(l)-1 , 0 , -1):
        x = l[i - 1].xcor()
        y = l[i - 1].ycor()
        l[i].goto(x,y)


    #to move the segment 0 to where the head is 
    if len(l) > 0:
        x = head.xcor()
        y = head.ycor()
        l[0].goto(x,y)


    move()

    #check for collision of head with body
    for i in l:
        if i.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #hide body
            for i in l:
                i.goto(1000,1000)

            #clear list 
            l.clear()

            #reset the score
            score = 0

            #reset the delay
            delay = 0.1

        
            pen.clear() #so it dosent overwrite
            pen.write("Score : {} High Score : {}".format(score,high_score), align = "center" , font = ("Courier" , 24 , "normal"))

    time.sleep(delay) #to create delay so the snake does not move faster than we can see



win.mainloop()