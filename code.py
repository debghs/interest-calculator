import matplotlib.pyplot as plt

def interest(principal, days,freq):
  if days <= 7:
    rate = 3.0
  elif days <= 14:
    rate = 3.0
  elif days <= 30:
    rate = 3.5
  elif days <= 45:
    rate = 4.5
  elif days <= 60:
    rate = 4.5
  elif days <= 89:
    rate = 4.5
  elif days <= 182:
    rate = 5.75
  elif days <= 273:
    rate = 6.0
  elif days <= 365:
    rate = 6.6
  elif days <= 547.5:
    rate = 7.1
  elif days <= 630:
    rate = 7.25
  elif days <= 730:
    rate = 7.0
  elif days <= 767:
    rate = 7.0
  elif days <= 1055:
    rate = 7.15
  elif days <= 1095:
    rate = 7.0
  elif days <= 1460:
    rate = 7.0
  elif days <= 1680:
    rate = 7.2
  elif days <= 1720:
    rate = 7.0
  else:
    rate = 7.0
  return principal * (1 + rate / (100.0 * freq)) ** ((days * freq) / 365.0) - principal

days = range(1, 3651)
principal = int(input("enter the principal = "))
freq = int(input("enter the cumulation frequency = "))
final_principal = [principal + interest(principal, d, freq) for d in days]
daily_interest = [interest(principal, d, freq) / d for d in days]

plt.subplot(2,1,1)
plt.plot(days, final_principal, label="Final Principal")
plt.ylabel("Amount")
plt.title("Capital")
plt.legend()
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(days, daily_interest, label="Daily Interest")
plt.xlabel("Days")
plt.ylabel("Rate")
plt.title("Daily Interest over Time")
plt.grid(True)
plt.show()


