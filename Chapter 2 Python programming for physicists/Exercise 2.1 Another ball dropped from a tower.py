# Done

def ball_drop(height):
    """
    this object calculates the time it takes for a ball
    to hit the ground when dropped from a tower of height
    in meters ignoring air resistance
    """
    tower_height = float(height)
    gravity = 9.81
    
    time_it_takes = (( 2 * tower_height )/ gravity)**(1/2)
    return time_it_takes

print(ball_drop(input("Enter the height of the tower in meters: ")))
