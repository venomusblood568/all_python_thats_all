import turtle                       #turtle is a pre-installed Python library that enables users to create pictures and shapes by providing them with a virtual canvas
sc = turtle.Screen()                #this is the screen 
sc.setup(1000,1000)                 #it's the screen size
spiral = turtle.Turtle()            #this is call function or statement    
spiral.speed(10)                    #defining speed
sc.bgcolor("black")                 #defing background color
col = ["yellow","red","purple","green"]   #we are saying the color going to use   
c = 0                                       # we are saying till when you have to run
for i in range(300):                        #this is a range or you can say time till when this will run
    spiral.forward(i*10)                    #this is path arrow is going to follow 
    spiral.right(144)                           #this is path arrow is going to follow 
    spiral.color(col[c])                        #we saying to use coulor of (col) in c to make that shape
    if c==3:                                          # i cant understand the line 13 to 16 i will update later                  
        c = 0
    else:
        c += 1