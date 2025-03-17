from random import choice

class RandomWalk:
    """A class to generate random walks."""
    
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self, restrict_direction=False):
        """
        Determine the direction and distance for a single step.
        
        Parameters:
        restrict_direction (bool): If True, only allow positive movement in x-direction.
        
        Returns:
        int: The step value (direction * distance).
        """
        if restrict_direction:
            direction = choice([1])  # Only move in the positive direction
        else:
            direction = choice([-1, 1])  # Move in either positive or negative direction
        
        distance = choice(range(9))  # Distance choices from 0 to 8
        step = direction * distance
        return step

    def fill_walk(self):
        """Calculate all the points in the walk."""
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            # Get steps for x and y directions using get_step()
            x_step = self.get_step(restrict_direction=True)  # Restrict x-direction to positive
            y_step = self.get_step()  # Allow y-direction to move both up and down
            
            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue
            
            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)
