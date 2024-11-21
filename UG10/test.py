from UG10_python import konser

print(f"Test Case 1: {konser('Tiket A', 'Jakarta', 36) == 1_880_000}") #nilai 25
print(f"Test Case 2: {konser('Tiket B', 'Surabaya', 11) == 1_375_000}") #nilai 25
print(f"Test Case 3: {konser('Tiket C', 'Bandung', 24) == 1_130_000}") #nilai 25
print(f"Test Case 4: {konser('Tiket A', 'Yogyakarta', 0) == 350_000}") #nilai 25