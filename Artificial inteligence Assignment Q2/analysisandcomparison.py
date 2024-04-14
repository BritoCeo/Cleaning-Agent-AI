import random
import time
import hillclimbing_algorithm


# Function to measure the execution time of the hill climbing algorithm
def measure_execution_time(places, distances):
    start_time = time.time()
    best_route, best_distance = hillclimbing_algorithm.hill_climbing(places, distances)
    end_time = time.time()
    return end_time - start_time, best_route, best_distance


# Run hill climbing algorithm on various test cases
test_cases = {
    "Test Case 1": {
        "places": ['Dorado Park', 'Khomasdal', 'Katutura', 'Eros', 'Klein Windhoek'],
        "distances": {
            'Dorado Park': {'Dorado Park': 0, 'Khomasdal': 7, 'Katutura': 20, 'Eros': 15, 'Klein Windhoek': 12},
            'Khomasdal': {'Dorado Park': 10, 'Khomasdal': 0, 'Katutura': 6, 'Eros': 14, 'Klein Windhoek': 18},
            'Katutura': {'Dorado Park': 20, 'Khomasdal': 6, 'Katutura': 0, 'Eros': 15, 'Klein Windhoek': 30},
            'Eros': {'Dorado Park': 15, 'Khomasdal': 14, 'Katutura': 25, 'Eros': 0, 'Klein Windhoek': 2},
            'Klein Windhoek': {'Dorado Park': 12, 'Khomasdal': 18, 'Katutura': 30, 'Eros': 2, 'Klein Windhoek': 0}
        }
    },
    # Define additional test cases if needed
}

for case_name, case_data in test_cases.items():
    places = case_data["places"]
    distances = case_data["distances"]

    execution_time, best_route, best_distance = measure_execution_time(places, distances)

    print(f"{case_name}:")
    print("Execution Time:", execution_time, "seconds")
    print("Best Route:", best_route)
    print("Total Distance:", best_distance)
    print("------------------------------------------")
