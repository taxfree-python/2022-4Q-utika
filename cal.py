import math

f_1 = [0.0002364, -0.001537, 0.9829]
f_2 = [0.0002461, -0.001657, 0.9832]
f_3 = [0.0002415, -0.001584, 0.9829]

def cal_axis_of_symmetry(a, b):
    return - b / 2 / a

def cal_top(a, b, c):
    return - (b **2 - 4 * a * c)/ 4 / a

def scaler_jup2SI_weight(m): #to gram
    return 1.90 * 1e30 * m

def scaler_sun2SI_length(l): #to m
    return 6.957 * 1e5 * 1e3 * l

def cal_radius(r_0, f):
    return r_0 * math.sqrt(f) * 1e-1

def cal_density(m, r_0, f):#to g,m-3
    return (3 * m) / (4 * math.pi * r_0 ** 3 * f * math.sqrt(f)) * 1e-3

# print(round(cal_axis_of_symmetry(f_1[0], f_1[1]), 3), round(cal_axis_of_symmetry(f_2[0], f_2[1]), 3), round(cal_axis_of_symmetry(f_3[0], f_3[1]), 4))
# print(round(1 - cal_top(f_1[0], f_1[1], f_1[2]), 5) * 100, round(1 - cal_top(f_2[0], f_2[1], f_2[2]), 5) * 100, round(1 - cal_top(f_3[0], f_3[1], f_3[2]), 5) * 100)


# count = [31533, 35054, 30622, 37974, 34801, 41725, 37578, 33324, 33813, 32000, 33635, 33579, 33672, 31635, 34988, 34022, 30024, 36000]
# print(sum(count) / len(count))

r_0 = 1.44
m = 2.1
f = (1.960 + 1.959 + 1.970) / 3
print(scaler_sun2SI_length(r_0))
print(f'r = {round(cal_radius(scaler_sun2SI_length(r_0), f), -5) / 1e8}')
print(f'd = {round(cal_density(scaler_jup2SI_weight(m), scaler_sun2SI_length(r_0), f), 3)}')
print(f'd_calibration = {cal_density(scaler_jup2SI_weight(m), scaler_sun2SI_length(r_0), f) * (cal_radius(scaler_sun2SI_length(r_0), f) / (69911 * 1e3) / 1.603) ** 3}')
print(f'{(cal_radius(scaler_sun2SI_length(r_0), f) / (69911 * 1e3))}')
print(f)