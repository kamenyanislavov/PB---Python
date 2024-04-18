movie_name = input()

student_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_tickets = 0

while movie_name != 'Finish':

    empty_seats = int(input())
    ticket_type = input()
    ticket_counter = 0

    while ticket_type != 'End':

        if ticket_type == 'Finish':
            break

        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kid_tickets += 1

        ticket_counter += 1

        if ticket_counter >= empty_seats:
            break

        ticket_type = input()

    print(f'{movie_name} - {ticket_counter / empty_seats * 100:.2f}% full.')

    if ticket_type == 'Finish':
        break
    else:
        movie_name = input()

total_tickets = student_tickets + standard_tickets + kid_tickets

print(f'Total tickets: {total_tickets}')
print(f'{student_tickets / total_tickets * 100:.2f}% student tickets.')
print(f'{standard_tickets / total_tickets * 100:.2f}% standard tickets.')
print(f'{kid_tickets / total_tickets * 100:.2f}% kids tickets.')
