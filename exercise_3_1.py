hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter the Rate:")
frate = float(rate)

if hrs <= 40:
    print(h * frate)
elif hrs > 40:
    print(40 * frate + (h - 40)*1.5*frate)
