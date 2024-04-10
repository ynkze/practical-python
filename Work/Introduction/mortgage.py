# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:        
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    month += 1

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    
    print(month, f'{total_paid:.2f}', f'{principal:.2f}')

if principal < 0:
    total_paid += principal
    principal = 0    

print(f'Total paid {total_paid:.2f}')
print('Months ', month)
