def turn_right():
    turn_left()
    turn_left()
    turn_left() 
    
def jump():
    if wall_in_front():
        turn_left()
        if wall_on_right():
          move()
          
        else:
          turn_right()  
        
    elif wall_on_right():
        move()
        
    else:
        move()
        
    
            
while not at_goal():
      jump()
        
        
        
        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
