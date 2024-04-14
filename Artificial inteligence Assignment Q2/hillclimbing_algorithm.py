import random

# Function to generate a random initial route visiting all places
def generate_initial_route(places):
    route = places[:]  # Make a copy of places list
    random.shuffle(route)  # Shuffle the route randomly
    return route

# Function to explore neighboring solutions by swapping the order of two randomly chosen places in the current route
def explore_neighbors(route):
    # Randomly select two indices
    i, j = random.sample(range(len(route)), 2)
    # Swap the places at the selected indices
    route[i], route[j] = route[j], route[i]
    return route

# Function to evaluate the total distance of a route
def calculate_total_distance(route, distances):
    total_distance = 0
    for i in range(len(route) - 1):
        start = route[i]
        end = route[i + 1]
        total_distance += distances[start][end]
    return total_distance

# Hill climbing algorithm for TSP
def hill_climbing(places, distances):
    # Generate a random initial route
    current_route = generate_initial_route(places)
    current_distance = calculate_total_distance(current_route, distances)

    # Store the initial route
    initial_route = current_route[:]

    # Repeat until reaching a local optimum
    while True:
        # Explore neighboring solution
        neighbor_route = explore_neighbors(current_route[:])
        neighbor_distance = calculate_total_distance(neighbor_route, distances)

        # If the neighbor's distance is better, move to the neighbor
        if neighbor_distance < current_distance:
            current_route = neighbor_route[:]
            current_distance = neighbor_distance
            # Store the intermediate route
            intermediate_route = current_route[:]
        else:
            # If no improving neighbors are found, return the final route
            final_route = current_route[:]
            final_distance = current_distance
            return initial_route, intermediate_route, final_route, final_distance

# Define the names of the places
places = ['Dorado Park', 'Khomasdal', 'Katutura', 'Eros', 'Klein Windhoek']

# Define the distance matrix
distances = {
    'Dorado Park': {'Dorado Park': 0, 'Khomasdal': 7, 'Katutura': 20, 'Eros': 15, 'Klein Windhoek': 12},
    'Khomasdal': {'Dorado Park': 10, 'Khomasdal': 0, 'Katutura': 6, 'Eros': 14, 'Klein Windhoek': 18},
    'Katutura': {'Dorado Park': 20, 'Khomasdal': 6, 'Katutura': 0, 'Eros': 15, 'Klein Windhoek': 30},
    'Eros': {'Dorado Park': 15, 'Khomasdal': 14, 'Katutura': 25, 'Eros': 0, 'Klein Windhoek': 2},
    'Klein Windhoek': {'Dorado Park': 12, 'Khomasdal': 18, 'Katutura': 30, 'Eros': 2, 'Klein Windhoek': 0}
}

# Run the hill climbing algorithm
initial_route, intermediate_route, final_route,final_distance= hill_climbing(places, distances)
print("Final Route:", final_route)
print("Total Distance:", final_distance)

import matplotlib.pyplot as plt


plt.figure(figsize=(8, 6))
plt.title('Initial Route')
for i in range(len(initial_route) - 1):
    plt.plot([initial_route[i], initial_route[i + 1]], [initial_route[i], initial_route[i + 1]], marker='o')
plt.show()

# Plot the intermediate routes
for i, route in enumerate(intermediate_route):
    plt.figure(figsize=(8, 6))
    plt.title(f'Intermediate Route {i + 1}')
    for i in range(len(route) - 1):
        plt.plot([route[i], route[i + 1]], [route[i], route[i + 1]], marker='o')
    plt.show()

# Plot the final route
plt.figure(figsize=(8, 6))
plt.title('Final Route')
for i in range(len(final_route) - 1):
    plt.plot([final_route[i], final_route[i + 1]], [final_route[i], final_route[i + 1]], marker='o')
plt.show()



