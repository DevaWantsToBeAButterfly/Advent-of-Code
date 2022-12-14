with open("data_files/day_6_input.txt") as input_file:
    orbit_pairs = []
    input_lines = input_file.readlines()
    for pair in input_lines:
        orbit_pairs.append(pair.replace("\n", ""))

orbits_map = {"COM": 0}
orbits_paths = {"COM": []}


def map_orbits(orbits_list):
    while orbits_list:
        new_orbits_list = []
        for orbit in orbits_list:
            [fixed_point, orbitant] = orbit.split(")")

            if fixed_point in orbits_map:
                orbits_map[orbitant] = orbits_map[fixed_point] + 1
                path_to_COM = [] + orbits_paths[fixed_point]
                path_to_COM.append(fixed_point)
                orbits_paths[orbitant] = path_to_COM

            else:
                new_orbits_list.append(orbit)

        orbits_list = new_orbits_list.copy()


def sum_orbits():
    total_orbits = 0

    for [mass, orbits] in orbits_map.items():
        total_orbits += orbits
    print(total_orbits)


def get_distance_to_santa():

    our_path = orbits_paths["YOU"]
    santa_path = orbits_paths["SAN"]
    shortest_path_to_santa = float("inf")

    for [node, distance] in orbits_map.items():
        if node in our_path and node in santa_path:

            our_distance = orbits_map["YOU"] - 1 - distance
            santa_distance = orbits_map["SAN"] - 1 - distance
            total_distance = our_distance + santa_distance

            if total_distance < shortest_path_to_santa:
                shortest_path_to_santa = total_distance

    print(shortest_path_to_santa)


map_orbits(orbit_pairs)
sum_orbits()
get_distance_to_santa()
