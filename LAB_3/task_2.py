# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, arg=','):
    participants_first_group = set(first_group.split(arg))
    participants_second_group = set(second_group.split(arg))

    common_participants = sorted(list(participants_first_group.intersection(participants_second_group)))

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)
if common_participants:
    print(f"Общие участники: {', '.join(common_participants)}")
else:
    print("Общих участников не найдено.")

# TODO Провеьте работу функции с разделителем отличным от запятой
