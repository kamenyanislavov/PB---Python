groups_of_climbers = int(input())  # the number of groups of climbers

total_num_climbers = 0
musala_climbers = 0
monblanc_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0

for x in range(groups_of_climbers):
    current_group = int(input())  # the number of climbers in the current group

    if current_group <= 5:
        musala_climbers += current_group
        total_num_climbers += current_group
    elif current_group <= 12:
        monblanc_climbers += current_group
        total_num_climbers += current_group
    elif current_group <= 25:
        kilimanjaro_climbers += current_group
        total_num_climbers += current_group
    elif current_group <= 40:
        k2_climbers += current_group
        total_num_climbers += current_group
    else:
        everest_climbers += current_group
        total_num_climbers += current_group

print(f'{musala_climbers / total_num_climbers * 100:.2f}%')
print(f'{monblanc_climbers / total_num_climbers * 100:.2f}%')
print(f'{kilimanjaro_climbers / total_num_climbers * 100:.2f}%')
print(f'{k2_climbers / total_num_climbers * 100:.2f}%')
print(f'{everest_climbers / total_num_climbers * 100:.2f}%')
