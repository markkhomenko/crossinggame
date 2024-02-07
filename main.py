######################################################
# Project: Project 2
# UIN: <654046372>
# repl.it URL: <https://replit.com/@CS111-Fall2021/Project-2-Imran54#main.py>

# ######################################################
# imports
import turtle
import random
# function definitions

def main():
  '''has all the program of the game incluing end screen'''
  
  # making the turtle and the screen
  s = turtle.Screen()
  t1 = turtle.Turtle()
  t1.ht()
  t2 = turtle.Turtle()
  t2.ht()


  

  s.setup(320,320)
  s.screensize(300,300)
  s.tracer(0)
  s.bgpic('background.gif')# set the screen background to the gif

  w,h = s.screensize() 

  # t1 = turtle.Turtle()
  # t1.penup()
  # t1.goto(-20,40)
  # t1.write('Spiderman VS Venom')
  # t1.goto(-40,-20)
  # t1.write('Press any key to Start')

  # input()
  # s.clear()
  # <variable declarations >
  # w = 300
  # h = 300
  # y = -100
  # y2 = -50
  # y3 = 0
  # y4 = 50
  # y5 = 100


  #making the variables
  x = -150
  sp1 = .1
  sp2 = .05
  sp3 = .125
  sp4 = .075
  sp5 = .175

  '''Making the variables for further use'''
 
  # list = [x , y]
  # print (list)

  # making the dictionaris for the game objects
  '''Making dictionaries and appending more in the dictionary made'''

  game_objects = [{'t':turtle.Turtle(), 'x':0, 'y':-100, 'radius': 10, 'image':'venom1.gif', 'type': 'a' }]
  game_objects.append({'t':turtle.Turtle(), 'x':20, 'y':-50, 'radius': 10, 'image':'venom2.gif', 'type': 'b' })
  game_objects.append({'t':turtle.Turtle(), 'x':-70, 'y':0, 'radius': 10, 'image':'venom3.gif', 'type': 'c' })
  game_objects.append({'t':turtle.Turtle(), 'x':90, 'y':50, 'radius': 10, 'image':'venom4.gif', 'type': 'd' })
  game_objects.append({'t':turtle.Turtle(), 'x':-130, 'y':100, 'radius': 10, 'image':'venom5.gif', 'type': 'e' })
  game_objects.append({'t':turtle.Turtle(), 'x':0, 'y':140, 'radius': 10, 'image':'batman.gif', 'type': 'batman' })
  game_objects.append({'t':turtle.Turtle(), 'x':0, 'y':-150, 'radius': 10, 'image':'spiderman2.gif', 'type': 'player' })
  
  
  # print (game_objects)

  # print (game_objects[4]['radius'])
  
  # coverting the turtle to the image
  '''Converting the turtle to the pictures'''
  for obj in game_objects:
    s.addshape(obj['image'])
    obj['t'].shape(obj['image'])
    # print (obj['image'])

  # print (game_objects[4]['t'].distance (game_objects[5]['t']))
    
  #    <keypress event handler>  # declared inside main due to scope issues

  '''Intializing the key press on the up, down, left, right'''  

  for obj in game_objects:
    if (obj['type'] ==  'player'):
      def left():
        obj['x'] -= 40
      def right():
        obj['x'] += 40
      def up():
        obj['y'] += 50
      def down():
        obj['y'] -= 50
      
    
  s.listen()
  s.onkey(left,'Left')
  s.onkey(right,'Right')
  s.onkey(up,'Up')
  s.onkey(down, 'Down')
  

 

  game_mode = 'play'
  lives = 3
  points = 0
  level = 1


  
  
  
  # def change_gamemode():
  #  main()

  



  # if game_mode == 'over':
  #   s.clear()
  #   s.bgpic('background.gif')
  #   t1.penup()
  #   t1.goto(-20,40)
  #   t1.write('Spiderman VS Venom')
  #   t1.goto(-40,-20)
  #   t1.write('Press J key to Start')
  #   s.listen()
  #   s.onkey(change_gamemode,'J'or 'j') 


  
  



  
  # animation loop

  while (game_mode != 'over') and (lives>0) and (lives < 4):

    for obj in game_objects:
      obj['t'].clear()

    for obj in game_objects:
      '''Setting the speeds of the objects by using the variable'''
      if (obj['type']== 'a'):
        obj['x'] += sp1
      elif (obj['type']== 'b'):
        obj['x'] -= sp2
      elif (obj['type']== 'c'):
        obj['x'] += sp3
      elif (obj['type']== 'd'):
        obj['x'] -= sp4
      elif (obj['type']== 'e'):
        obj['x'] += sp5
      
    for obj in game_objects:
      '''Making the objects start again and not run off the screen'''
      if (obj['type'] == 'a') and obj['x']> (150 + obj['radius']):
        obj["x"] = -150
      elif (obj['type'] == 'b') and obj['x']<(-150 - obj['radius']):
        obj["x"] = 150
      elif (obj['type'] == 'c') and obj['x']> (150 + obj['radius']):
        obj["x"] = -150
      elif (obj['type'] == 'd') and obj['x']< (-150 - obj['radius']):
        obj["x"] = 150
      elif (obj['type'] == 'e') and obj['x']> (150 + obj['radius']):
        obj["x"] = -150
      elif (obj['type'] == 'player') and obj['x']> (150 + obj['radius']):
        obj["x"] = 150
      elif (obj['type'] == 'player') and obj['x']< (-150 - obj['radius']):
        obj["x"] = -150
      elif (obj['type'] == 'player') and obj['y']< (-150 - obj['radius']):
        obj["y"] = -150
      elif (obj['type'] == 'player') and obj['y'] > (150 + obj['radius']):
        obj["y"] = 150
      
      

      t = obj["t"]
      x = obj["x"]
      y = obj["y"]
      # t.penup()
      t.goto(x, y) 
      # t.pendown()

    
    #printing the lives on the screen at the beginning 
    t2.penup()
    t2.goto(125,140)
    t2.color("purple")
    t2.pendown()
    t2.clear()
    t2.write(f'Lives:{lives}',font= 'Arial', align = 'right')

    '''Printing the points on the screen'''
    t1.penup()
    t1.goto(-125,140)
    t1.color("white")
    t1.pendown()
    t1.clear()
    t1.write(f'Points:{points}',font= 'Arial', align = 'left')



    


    
    #collisions and their implementation

    for obj in game_objects:
      
     if (game_objects[0]['t'].distance(game_objects[6]['t']) < (20)):
       game_objects[6]['t'].goto(0,-150)
       game_objects[6]['x'] = 0
       game_objects[6]['y'] = -150
       lives-=1
       t1.penup()
       t1.goto(125,140)
       t1.color("purple")
       t1.pendown()
       t1.clear()
       t1.write(f'Lives:{lives}',font= 'Arial', align = 'right')
     elif (game_objects[1]['t'].distance(game_objects[6]['t']) < (20)):
        game_objects[6]['t'].goto(0,-150)
        game_objects[6]['x'] = 0
        game_objects[6]['y'] = -150
        lives-=1
        t1.penup()
        t1.goto(125,140)
        t1.color("purple")
        t1.pendown()
        t1.clear()
        t1.write(f'Lives:{lives}',font= 'Arial', align = 'right')
     elif (game_objects[2]['t'].distance(game_objects[6]['t']) < (20)):
        game_objects[6]['t'].goto(0,-135)
        game_objects[6]['x'] = 0
        game_objects[6]['y'] = -150
        lives-=1
        t1.penup()
        t1.goto(125,140)
        t1.color("purple")
        t1.pendown()
        t1.clear()
        t1.write(f'Lives:{lives}',font= 'Arial', align = 'right')
     elif (game_objects[3]['t'].distance(game_objects[6]['t']) < (20)):
        game_objects[6]['t'].goto(0,-150)
        game_objects[6]['x'] = 0
        game_objects[6]['y'] = -150
        lives-=1
        t1.penup()
        t1.goto(125,140)
        t1.color("purple")
        t1.pendown()
        t1.clear()
        t1.write(f'Lives:{lives}',font= 'Arial', align = 'right')
     elif (game_objects[4]['t'].distance(game_objects[6]['t']) < (20)):
       game_objects[6]['t'].goto(0,-150)
       game_objects[6]['x'] = 0
       game_objects[6]['y'] = -150
       lives-=1
       t1.penup()
       t1.goto(125,140)
       t1.color("purple")
       t1.pendown()
       t1.clear()
       t1.write(f'Lives:{lives}',font= 'Arial', align = 'right')
     elif (game_objects[5]['t'].distance(game_objects[6]['t']) < (30)):
       game_objects[6]['t'].goto(0,-150)
       game_objects[6]['x'] = 0
       game_objects[6]['y'] = -150
       points += 20
       level += 1
       sp1 += .05
       sp2+= .05
       sp3 += .05
       sp4 += .05
       sp5 += .05  
       game_objects[5]['x'] = random.randint(-150,150) 
       t1.penup()
       t1.goto(-125,140)
       t1.color("white")
       t1.pendown()
       t1.clear()
       t1.write(f'Points:{points}',font= 'Arial', align = 'left')
#    <start screen> 
#    <game over screen>


    s.update()
  # if lives equal to zero
  if lives == 0:
    s.clear()
    s.bgpic('background.gif')
    t1.penup()
    t1.goto(-40,20)
    t1.write('Game Over')
    t1.goto(-40,-20)
    t1.write('Score: ' + str(points))

'''Another function for the start of the game'''
def start():
  print ('Made by Imran Khan')
  s = turtle.Screen()
  t3 = turtle.Turtle()
  t3.ht()
  

  x = 'over'
    

  s.setup(320,320)
  s.screensize(300,300)
  s.tracer(0)
  s.bgpic('background.gif')

  '''starts the main function'''
  def change_gamemode():
    s.clear()
    main()
    


  if x == 'over':
    s.clear()
    s.bgpic('background.gif')
    t3.penup()
    t3.goto(-50,40)
    t3.write('Spiderman VS Venom')
    t3.goto(-50,-20)
    t3.write('Press Space key to Start')
    s.listen()
    s.onkey(change_gamemode,'space') 
    
start()