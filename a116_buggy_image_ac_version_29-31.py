# a116_buggy_image.py
import turtle as trtl
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
#spider body

legs = 8  
leg_length = 70
leg_angle = 360 / legs 
#config legs

spider.pensize(5)
leg_angle_diff = 0
while (leg_angle_diff < legs // 2):
    spider.penup()
    spider.goto(0, 20)
    spider.setheading(230 - (leg_angle_diff * 30))  
    spider.pendown()
    spider.forward(leg_length)
    leg_angle_diff = leg_angle_diff + 1

leg_angle_diff = 0
while (leg_angle_diff < legs // 2):
    spider.penup()
    spider.goto(0, 20)
    spider.setheading(-45 + (leg_angle_diff * 30))  
    spider.pendown()
    spider.forward(leg_length)
    leg_angle_diff = leg_angle_diff + 1
#draw legs

spider.penup()
spider.pencolor("white")
spider.goto(-10, -10)  
spider.pendown()
spider.pensize(10)
spider.circle(2)  

spider.penup()
spider.goto(10, -10)  
spider.pendown()
spider.circle(2)
#draw eyes

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()