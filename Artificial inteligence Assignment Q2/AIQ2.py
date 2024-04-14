

# Problem Representation (20%)
class Graph:
    def __init__(self, places, distances):
        self.places = places  # List of place names
        self.distances = distances  # Distance matrix

    #function to calculate total distance of route
    def calculate_total_distance(self, route):
        total_distance = 0
        for i in range(len(route) - 1):
            start = route[i]
            end = route[i + 1]
            total_distance += self.distances[start][end]
        return total_distance


# Locations
places = ['Dorado Park', 'Khomasdal', 'Katutura', 'Eros', 'Klein Windhoek']

# Distance matrix
distance_matrix = {
    'Dorado Park': {'Dorado Park': 0, 'Khomasdal': 7, 'Katutura': 20, 'Eros': 15, 'Klein Windhoek': 12},
    'Khomasdal': {'Dorado Park': 10, 'Khomasdal': 0, 'Katutura': 6, 'Eros': 14, 'Klein Windhoek': 18},
    'Katutura': {'Dorado Park': 20, 'Khomasdal': 6, 'Katutura': 0, 'Eros': 15, 'Klein Windhoek': 30},
    'Eros': {'Dorado Park': 15, 'Khomasdal': 14, 'Katutura': 25, 'Eros': 0, 'Klein Windhoek': 2},
    'Klein Windhoek': {'Dorado Park': 12, 'Khomasdal': 18, 'Katutura': 30, 'Eros': 2, 'Klein Windhoek': 0}
}

#  graph instance
graph = Graph(places, distance_matrix)

# Example
route = ['Dorado Park', 'Khomasdal', 'Katutura', 'Eros', 'Klein Windhoek']  # Example route visiting all places
total_distance = graph.calculate_total_distance(route)
print("Total distance:", total_distance)

