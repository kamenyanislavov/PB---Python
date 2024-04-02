deposited_sum = float(input())
period = int(input())
interest_rate = float(input())

annual_interest_rate = interest_rate / 100
final_sum = deposited_sum + period * ((deposited_sum * annual_interest_rate) / 12)

print(final_sum)
