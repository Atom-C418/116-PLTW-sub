#   a116_buggy_image.py
import turtle as trtl
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
#spider body

legs = 6
leg_length = 70
leg_angle = 380 / legs
#config legs

spider.pensize(5)
leg_angle_diff = 0
while (leg_angle_diff < legs):
  spider.goto(0,0)
  spider.setheading(leg_angle*leg_angle_diff)
  spider.forward(leg_length)
  leg_angle_diff = leg_angle_diff + 1
#draw legs

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()