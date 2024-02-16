import matplotlib.pyplot as plt

def interest(principal, days,freq):
  """
  Calculates the interest earned on a principal amount for a given number of days.

  Args:
    principal: The initial principal amount.
    days: The number of days.

  Returns:
    The interest earned.
  """
  if days <= 7:
    rate = 3.0
  elif days <= 14:
    rate = 3.0
  elif days <= 29:
    rate = 3.0
  elif days <= 45:
    rate = 3.5
  elif days <= 60:
    rate = 4.25
  elif days <= 90:
    rate = 4.5
  elif days <= 120:
    rate = 4.75
  elif days <= 150:
    rate = 4.75
  elif days <= 184:
    rate = 4.75
  elif days <= 210:
    rate = 5.75
  elif days <= 270:
    rate = 5.75
  elif days <= 289:
    rate = 6.0
  elif days <= 365:
    rate = 6.0
  elif days <= 389:
    rate = 6.70
  elif days <= 455:
    rate = 6.70
  elif days <= 545:
    rate = 7.20
  elif days <= 730:
    rate = 7.20
  elif days <= 3*365:
    rate = 7.0
  elif days <= 5*365:
    rate = 7.0
  else:
    rate = 6.90
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


