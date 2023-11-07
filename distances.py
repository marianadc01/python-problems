import random
import math
import string
import matplotlib.pyplot as plt

# Constants for the region of interest (ROI)
lat_min = 38.7 # minimum latitude in decimal degrees
lat_max = 38.78 # maximum latitude in decimal degrees
lon_min = -9.2 # same for longitude
lon_max = -9.1
coef_lat = 111120 # 1 degree of latitude corresponds approx to 111120 meters
coef_lon = 86672 # 1 degree of longitude corresponds approx to 86672 meters at this latitude

def main():
    N = get_integer("Number of points: ", 2, 10)
    option = get_string("User provided (u) or random (r): ",["u","r"])
    # Create dictionary of coordinates
    d = get_coordinates(N, option)
    # Determine pair of points farthest apart
    max_dist = 0
    for name_1,P1 in d.items():
        for name_2,P2 in d.items():
            distance = compute_distance(P1,P2)
            if distance >= max_dist:
                max_dist = distance
                point_1, point_2 = name_1, name_2
    print(f"{point_1} and {point_2} are farthest apart")
    plot_scatter(d)

# input dictionary of points
# side effect: scatter plot of points with labels
def plot_scatter(points: dict):
    x_vals = [point[0] for point in points.values()]
    y_vals = [point[1] for point in points.values()]
    plt.scatter(x_vals, y_vals)
    plt.xlabel('Lon')
    plt.ylabel('Lat')
    plt.title('Scatter Plot of Points')
    for label, point in points.items():
        plt.annotate(label, point, textcoords='offset points', xytext=(0, 10))
    plt.grid(True)
    plt.show()


# input: string (prompt to user), float (minimum value for input), float (maximum value for input)
# output: float (user's provided value between minimum and maximum)
# side effect: keeps asking for input until the user provides a valid input
def get_decimal(prompt: str,Min: float, Max: float) -> float:

    while True: # why not to ask for input for lon and lat separately? 
        try:
            coordinate = float(input(prompt))
            if Min <= coordinate <= Max: 
                return coordinate

        except ValueError: 
            pass   



# input: string (prompt to user), integer (minimum value for input), integer (maximum value for input)
# output: integer (user's provided value between minimum and maximum)
# side effect: keeps asking for input until the user provides a valid input
def get_integer(prompt: str,Min: int, Max: int) -> int:

    while True:
        try:
            N = int(input("Number of points: "))
            if Min <= N <= Max:
                return N
            else:
                print(f"Choose in a range of {Min} and {Max}")
                pass

        except ValueError:
            print(f"Choose in a range of {Min} and {Max}")
            pass

    

# input: string (prompt to user), list (list of strings that are acceptable values)
# output: string (user's provided value among the values in L)
# side effect: keeps asking for input until the user provides a valid input
def get_string(prompt: str,L: list) -> str:

    while True:
        try:
            option = input("User provided (u) or random (r): ")
            if option in L:
                return option
            else: 
                pass
            
        except ValueError: 
            pass    

# inputs: integer (number of points), string (option: user provided "u" or random "r")
# output: dictionary of points. The key is the point name and the value is a tuple lon,lat in decimal degrees
# hint: call get_decimal
def get_coordinates(N: int, option: str) -> dict:
    
    d = {}

    for items in range(1, N + 1): # why not in range(N)
        name = input("Point name: ")
        if option == "u": 
                lon = get_decimal("Enter value between -9.2 and -9.1: ", lon_min, lon_max)
                lat = get_decimal("Enter value between 38.7 and 38.78: ", lat_min, lat_max)

        else:
                lon = random.uniform(lon_min, lon_max)
                lat = random.uniform(lat_min, lat_max)
        d[name] = (lon, lat)

    return d

# input: tuple (lon,lat for 1st point), tuple (lon,lat for 2nd point)
# output: float (approximate distance in meters between P1 and P2)
def compute_distance(P1: tuple, P2: tuple) -> float:
    # for name in d:
    # why do we need P1 and P2?? 
    lon1, lat1 = P1
    lon2, lat2 = P2
        # P1 = (d[name][0], d[name][1])
        # P2 = (d[name+1][0], d[name+1][1])

    dif_lon = (lon1 - lon2)*coef_lon
    dif_lat = (lat1 - lat2)*coef_lat
    distance = math.sqrt(dif_lat**2 + dif_lon**2)

    return distance


main()
