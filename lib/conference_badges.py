def badge_maker(Tobias):
    return f"Hello, my name is {Tobias}."
print(badge_maker)

def batch_badge_creator(names):
    badge_messages = []
    for name in names:
        badge_messages.append(f"Hello, my name is {name}.")
    return badge_messages


def assign_rooms(speakers):
    room_assignments = []
    for index, speaker in enumerate(speakers, start=1):
        room_assignments.append(f"Hello, {speaker}! You'll be assigned to room {index}!")
    return room_assignments


def printer(speakers):
    badge_messages = batch_badge_creator(speakers)
    for message in badge_messages:
        print(message)
    room_assignments = assign_rooms(speakers)
    for assignment in room_assignments:
        print(assignment)
