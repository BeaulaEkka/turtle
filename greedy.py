# greedy Algorithms Tutorial
# Bulbs
'''given N bulbs, itther on (1) or off(0).
Turning on ith bulb causes all remaining bulbs on the right to flip.

Find the min number of switches to turla all the bulbs on.

constraints:
1>N<=1e5 # n of bulbs are between 1 and 10to the power 5
A[i]={0,1} # the bulb or the bit is 0 or 1

'''
# Traveling Salesperson
# from sys import maxsize
# from itertools import permutations
# from math import factorial
# V = 4


# def travellingSalesmanProblem(graph, s):
#     vertex = []
#     for i in range(V):
#         if i != s:
#             vertex.append(i)
import itertools


def calculate_distance(route, distances):
    """
    Calculate the total distance of a given route based on the distance matrix.
    """
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i + 1]]
    # Add distance to return to the starting city
    total_distance += distances[route[-1]][route[0]]
    return total_distance


def travelling_salesman_problem(cities, distances):
    """
    Solve the Travelling Salesman Problem using brute force.
    cities: List of city names
    distances: 2D list representing the distance matrix
    """
    n = len(cities)
    city_indices = list(range(n))
    shortest_distance = float('inf')
    best_route = None

    # Generate all permutations of cities
    for perm in itertools.permutations(city_indices):
        current_distance = calculate_distance(perm, distances)
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            best_route = perm

    # Convert indices back to city names
    best_route_cities = [cities[i] for i in best_route]
    return best_route_cities, shortest_distance


# Example usage:
cities = ["New Delhi", "Katmandu", "Agra" , "Calcutta"]
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_route, shortest_distance = travelling_salesman_problem(cities, distances)

print("Best route:", best_route)
print("Shortest distance:", shortest_distance)
