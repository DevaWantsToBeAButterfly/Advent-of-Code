class Vent:
    def __init__(self, name, steam, neighbours):
        self.name = name
        self.flow_rate = steam
        self.neighbours = neighbours
        self.was_opened = False
        self.distance_from_start = 999999999
        self.venting_potential = 0

    def replace_neighbours(self, vents):
        for index, neighbour in enumerate(self.neighbours):
            for vent in vents:
                if vent.name == neighbour:
                    self.neighbours[index] = vent

    def check_neighbours(self):
        neighbours_to_check = set()
        for neighbour in self.neighbours:
            if neighbour.distance_from_start > self.distance_from_start + 1:
                neighbour.distance_from_start = self.distance_from_start + 1
                neighbours_to_check.add(neighbour)

        return neighbours_to_check

    def calculate_venting_potential(self, current_round):
        self.venting_potential = self.flow_rate * (current_round - self.distance_from_start - 1)
        return self.venting_potential

vents = []
vents.append(Vent('AA', 0, ['DD', 'II', 'BB']))
vents.append(Vent('BB', 13, ['CC', 'AA']))
vents.append(Vent('CC', 2, ['DD', 'BB']))
vents.append(Vent('DD', 20, ['CC', 'AA', 'EE']))
vents.append(Vent('EE', 3, ['FF', 'DD']))
vents.append(Vent('FF', 0, ['EE', 'GG']))
vents.append(Vent('GG', 0, ['FF', 'HH']))
vents.append(Vent('HH', 22, ['GG']))
vents.append(Vent('II', 0, ['AA', 'JJ']))
vents.append(Vent('JJ', 21, ['II']))

for vent in vents:
    vent.replace_neighbours(vents)

vents_to_check = [vents[0]]
current_round = 30
total_venting = 0

while True:
    vents_to_check[0].distance_from_start = 0
    max_venting_potential = 0
    vent_to_go_to = None

    while vents_to_check:
        vent = vents_to_check[0]
        vents_to_check += (vent.check_neighbours())
        vents_to_check.remove(vent)

    for vent in vents:
        if vent.calculate_venting_potential(current_round) > max_venting_potential and \
                vent.distance_from_start < (current_round - 1) and not vent.was_opened:
            max_venting_potential = vent.venting_potential
            vent_to_go_to = vent

    if vent_to_go_to:
        current_round -= (vent_to_go_to.distance_from_start + 1)
        print(f'Opening vent {vent_to_go_to.name} on round {current_round}, venting {max_venting_potential} steam')
        total_venting += vent_to_go_to.venting_potential
        vents_to_check = [vent_to_go_to]
        vent_to_go_to.was_opened = True
        for vent in vents:
            vent.distance_from_start = 9999999
        vent_to_go_to.distance_from_start = 0

    else:
        break

# adjacency matrix using Floyd-Warshall

print(total_venting)