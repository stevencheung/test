
# Monthly interest rate
# = (Annual interest rate) / 12
# Monthly payment lower bound
# = Balance / 12
# Monthly payment upper bound
# = (Balance x (1 + Monthly interest rate)12) / 12
# The following variables contain values as described below:

# balance
# - the outstanding balance on the credit card
# annualInterestRate
# - annual interest rate as a decimal

balance = 100.0
annualInterestRate = 12.34

monthlyInterestRate = (annualInterestRate * 1.0)/12
 
min_p = (balance * 1.0)/12
max_p = (balance * pow(1 + monthlyInterestRate,12))/12
a = min_p
b = max_p
res = min_p
found = False

while not found:
   if (max_p - min_p) < 0.01:
       found = True
       res = min_p

   avg_p = (min_p + max_p) / 2.0
   tmp = balance

   for i in range(12):
      tmp = tmp * (1 + monthlyInterestRate)
      if tmp > avg_p:
          tmp = tmp - avg_p
      else:
          tmp = 0

   if tmp <= 0:
      max_p = avg_p
      print ("new max_p: " + str(max_p))
   else:
      min_p = avg_p
      print ("new min_p: " + str(min_p))

print (a, b, res)
