import turtle #we are sying for import of turtle 
t = turtle.Turtle() #When a Turtle object is created or a function derived from some Turtle method is called a TurtleScreen object is automatically created.
s = turtle.Screen() #Return the singleton screen object. If none exists at the moment, create a new one and return it, else return the existing one.
s.bgcolor("#262626") # we are calling for screen background and #262626 is color code of background color 
t.pencolor("#7C909C") # we are saying this is a color it is going to use as pen and #7C909C is color code 
t.speed(100) # we are defineing the speed of pen 
col = ("#ED7864","#6E544F","#592F2F","#6E382E") # color is is going to use for petal color
for n in range(5):  #range 5 denotes the no of time it is going to run or you can say it is no of layer of petal 
    for x in range(8): # range 8 denotes the no of petal 
        t.speed( x + 10 ) #speed means how fast it is going to make 
        for i in range(2): # 2 repesent the two sides of petal 
            t.pensize(2) # pensize
            t.circle(80+n*20,90) #for making circle we are using this 
            t.lt(90) #lt represnt the left size move and  you have see what if you put rt! and have fun
        t.lt(45) #same this too
    t.pencolor(col[n % 4]) # this will increase the size of the pen and as per color changing
s.exitonclick() # this will let the finish drawing on screen otherwise it will dispappere 