import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Make a random walk with 5,000 points.
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Plot the points in the walk using ax.plot().
    plt.style.use('classic')
    fig, ax = plt.subplots()
    
    #15.3 Plot the path of the random walk
    ax.plot(rw.x_values, rw.y_values, linewidth=2, c='blue')

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)  # Starting point
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)  # Ending point

    # Set aspect ratio and remove axes for a cleaner look.
    ax.set_aspect('equal')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    
    # Ask user if they want to make another walk.
    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break
