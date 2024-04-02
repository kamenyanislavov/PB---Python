pool_volume = int(input())
debit_pipe_1 = int(input())
debit_pipe_2 = int(input())
time = float(input())

volume_from_pipe_1 = debit_pipe_1 * time
volume_from_pipe_2 = debit_pipe_2 * time
water_volume = volume_from_pipe_1 + volume_from_pipe_2

if pool_volume >= water_volume:
    print('The pool is', '{:.2f}'.format(water_volume / pool_volume * 100) + '% full. Pipe 1:',
          '{:.2f}'.format(volume_from_pipe_1 / water_volume * 100) + '%. Pipe 2:',
          '{:.2f}'.format(volume_from_pipe_2 / water_volume * 100) + '%.')
else:
    print(f'For {time} hours the pool overflows with', '{:.2f}'.format(water_volume - pool_volume), 'liters.')
