favourite_book = input()
book = input()
book_counter = 0

while book != 'No More Books':
    book_counter += 1

    if book == favourite_book:
        break

    book = input()

if book == favourite_book:
    print(f'You checked {book_counter - 1} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {book_counter} books.')
