test_input = '''10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL'''

chemicals_dict = {}

class Chemical():
    def __init__(self, reaction_data):
        self.name = ''
        self.produced_amount = 0
        self.production_cost = {}
        self.translate_reaction(reaction_data)

    def translate_reaction(self, reaction_data):
        reaction = reaction_data.replace(',', '').split(' => ')
        output = reaction[1].split(' ')
        self.name = output[1]
        self.produced_amount = int(output[0])

        input = reaction[0].split(' ')
        for chem_count, chem_name in zip(input[::2], input[1::2]):
            self.production_cost[chem_name] = int(chem_count)


for line in test_input.splitlines():
    temp_chemical = Chemical(line)
    chemicals_dict[temp_chemical.name] = temp_chemical

for chem in chemicals_dict.values():
    print(chem.name, chem.produced_amount, chem.production_cost)
