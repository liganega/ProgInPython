import turtle as t

wn= t.Screen()


wn.tracer(10, 100)
player = t.Turtle()
dist = 2
for i in range(200):
    player.fd(dist)
    player.rt(90)
    dist += 2

wn.mainloop()
