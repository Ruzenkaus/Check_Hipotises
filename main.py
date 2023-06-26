import numpy as np
import scipy.stats as stats

deter = np.array([[50.3,49.9,48.9,47.6],
             [48.3,50.1,49.4,47.5],
             [47.1,50.3,46.3,50.8],
             [47.5,51.9,51.5,51.6],
             [52.1,51.2,50.9,49]]) #any of your matrix's
print(f"Matrix:\n{deter}")

x1 = deter[0].mean()
x2 = deter[1].mean()
x3 = deter[2].mean()
x4 = deter[3].mean()
x5 = deter[4].mean()
vidhl = np.array([x1, x2, x3, x4, x5])

print(f" x1:{deter[0].mean()} \n x2:{deter[1].mean()} \n x3:{deter[2].mean()} \n"
      f" x4:{deter[3].mean()} \n x5:{deter[4].mean()}")

_x = (x1 + x2 + x3 + x4 + x5) / 5

print(f"x**:{_x}")

Q1 = 4 * (pow((vidhl[0] - _x), 2) + pow((vidhl[1] - _x), 2) + pow((vidhl[2] - _x), 2)
          + pow((vidhl[3] - _x), 2)+pow((vidhl[4] - _x), 2))

print(f"Q1:{Q1}")

Q2 = 0

for zn in deter[0]:
    Q2 += pow(zn - vidhl[0], 2)

for zn in deter[1]:
    Q2 += pow(zn - vidhl[1], 2)

for zn in deter[2]:
    Q2 += pow(zn - vidhl[2], 2)

for zn in deter[3]:
    Q2 += pow(zn - vidhl[3], 2)

for zn in deter[4]:
    Q2 += pow(zn - vidhl[4], 2)


print(f"Q2:{Q2}")

s1_std = Q1 / (len(vidhl) - 1)
print(f"s1_std:{s1_std}")

s2_std = Q2 / ((len(deter[0]) + len(deter[1]) + len(deter[2]) + len(deter[3])+ len(deter[4])) - len(vidhl))
print(f"s2_std:{s2_std}")

Kspos = s1_std / s2_std
print(f"Kspos: {Kspos}")

Kkr = stats.f.ppf(1-0.05, (len(vidhl) - 1),
                  ((len(deter[0]) + len(deter[1]) + len(deter[2]) + len(deter[3])+len(deter[4])) - len(vidhl)))

print(f"Kkr:{Kkr}")


if Kspos > Kkr:
    print("H0 throws")
elif Kspos<Kkr:
    print("H1 throws")