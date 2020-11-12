#!/usr/bin/env python3
import turtle
import sys
import random
import math

def createPerson(height,width,circleradius,point,maxvelocity):
	#create a person and move them to a point
	p=turtle.Turtle()
	p.shape('circle')
	p.color('green')
	p.speed(0)
	p.penup()

	#this block of code sets up a dictionary of characteristics for a person
	person={}
	person['x']=point[0]
	person['y']=point[1]
	p.goto(person['x'],person['y'])

	#define velocity in x and y
	vx=random.uniform(-maxvelocity,maxvelocity)
	vy=random.uniform(-maxvelocity,maxvelocity)
	#r=list(range(-10,-6))+list(range(6,10))
	#vx=random.choice(r)
	#vy=random.choice(r)

	person['point']=p
	person['vx']=vx
	person['vy']=vy
	return(person)

steps=10000
stepsize=1

#variables that influence the outbreak
npeople=375
circlediam=20.0
width=700
height=700
maxvelocity=6

circleradius=circlediam/2

#create a window 
win=turtle.getscreen()
win.tracer(0)
### Uncomment below to have window be proportional to screen
#width=win.window_width()
#height=win.window_height()
t=turtle.Turtle()
t.hideturtle()

#draw bounding box
t.penup()
t.goto((-width-circlediam)//2,(-height-circlediam)//2)
t.pendown()
t.goto((width+circlediam)//2,(-height-circlediam)//2)
t.goto((width+circlediam)//2,(height+circlediam)//2)
t.goto((-width-circlediam)//2,(height+circlediam)//2)
t.goto((-width-circlediam)//2,(-height-circlediam)//2)
t.penup()

#set up the population in personlist
personlist=[]
print ("Populating simulation")
for n in range(npeople):
	point=(random.randint( (-width//2)+circleradius, (width//2)-circleradius), random.randint( (-height//2)+circleradius, (height//2)-circleradius))
	personlist.append(createPerson(height,width,circleradius,point,maxvelocity))
	
print("\nPopulating complete")


#do a loop where the circle moves according to the velocity

for n in range(steps):
	
	#take a step
	for person in personlist:
		dx=person['vx']*stepsize
		dy=person['vy']*stepsize
		
		newx=person['x']+dx
		newy=person['y']+dy
	
		#make circle bounce if it "hits" a wall. 
		if newx > width/2: #positive x wall
			newx=width/2
			person['vx']=person['vx']*-1
		elif newx < -width/2:
			newx=-width/2
			person['vx']=person['vx']*-1

		if newy > height/2:
			newy=height/2
			person['vy']=person['vy']*-1
		elif newy < -height/2:
			newy=-height/2
			person['vy']=person['vy']*-1

		person['x']=newx
		person['y']=newy
		person['point'].goto(newx,newy)
			
	win.update()
