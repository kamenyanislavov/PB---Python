user_input = input()

fruits = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']
vegetables = ['tomato', 'cucumber', 'pepper', 'carrot']

if user_input in fruits:
    print('fruit')
elif user_input in vegetables:
    print('vegetable')
else:
    print('unknown')
