import csv
import matplotlib.pyplot as plt
import numpy as np
from statistics import variance,stdev


with open('data.csv') as f:
    data = [row for row in csv.reader(f)]

time = [0] + [float(data[i][0]) * 100 - float(data[0][0]) * 100 for i in range(1, len(data))]

flux_rate = [float(data[i][2]) for i in range(len(data))]
time.pop(len(flux_rate) // 3 - 21)
flux_rate.pop(len(flux_rate) // 3 - 21)


start = 21
end = 331
ave = sum(flux_rate[:start] + flux_rate[end:]) / len(flux_rate[:start] + flux_rate[end:])
flux_rate = [flux_rate[i] / ave for i in range(len(flux_rate))]


window_size_1 = 5
flux_rate_modified_1 = [sum(flux_rate[i - window_size_1 // 2:i + window_size_1 // 2 + 1]) / window_size_1 for i in range(window_size_1 // 2, len(flux_rate) - window_size_1 // 2)]

window_size_2 = 9
flux_rate_modified_2 = [sum(flux_rate[i - window_size_2 // 2:i + window_size_2 // 2 + 1]) / window_size_2 for i in range(window_size_2 // 2, len(flux_rate) - window_size_2 // 2)]


# print(round(variance(flux_rate), 5), round(variance(flux_rate_modified_1), 5), round(variance(flux_rate_modified_2), 5))
# print(round(stdev(flux_rate[:start + 1] + flux_rate[end:]), 5), round(stdev(flux_rate_modified_1[:start + 1 - window_size_2 // 2] + flux_rate_modified_1[end - window_size_2 // 2:]), 5), round(stdev(flux_rate_modified_1[:start + 1 - window_size_2 // 2] + flux_rate_modified_1[end - window_size_2 // 2:]), 5))


# fit = np.polyfit(time, flux_rate, 2)
# fit = np.poly1d(fit)
# fit_1 = np.polyfit(time[window_size_1 // 2:len(flux_rate) - window_size_1 // 2], flux_rate_modified_1, 2)
# fit_1 = np.poly1d(fit_1)
# fit_2 = np.polyfit(time[window_size_2 // 2:len(flux_rate) - window_size_2 // 2], flux_rate_modified_2, 2)
# fit_2 = np.poly1d(fit_2)
fit = np.polyfit(time[start:end], flux_rate[start:end], 2)
fit = np.poly1d(fit)
fit_1 = np.polyfit(time[start:end], flux_rate_modified_1[start - window_size_1 // 2:end - window_size_1 // 2], 2)
fit_1 = np.poly1d(fit_1)
fit_2 = np.polyfit(time[start:end], flux_rate_modified_2[start - window_size_2 // 2:end - window_size_2 // 2], 2)
fit_2 = np.poly1d(fit_2)


fig = plt.figure(figsize = (12, 8))
ax = fig.add_subplot(1, 1, 1)

# plt.boxplot(flux_rate, vert = False)
# ax.set_yticklabels(['flux'], fontsize = 15)

ax.scatter(time, flux_rate, label = 'original(dropped)', color = 'm')
ax.scatter(time[window_size_1 // 2:len(flux_rate) - window_size_1 // 2], flux_rate_modified_1, label = 'window size = 5', color = 'g')
ax.scatter(time[window_size_2 // 2:len(flux_rate) - window_size_2 // 2], flux_rate_modified_2, label = 'window size = 9', color = 'y')

ax.plot(time, fit(time), label = 'fitting-original', linewidth = 2, color = 'm')
ax.plot(time[window_size_1 // 2:len(flux_rate) - window_size_1 // 2], fit_1(time[window_size_1 // 2:len(flux_rate) - window_size_1 // 2]), label = 'fitting-5', linewidth = 2, color = 'g')
ax.plot(time[window_size_1 // 2:len(flux_rate) - window_size_1 // 2], fit_2(time[window_size_1 // 2:len(flux_rate) - window_size_1 // 2]), label = 'fitting_9', linewidth = 2, color = 'y')

ax.axvline(3.250846023688663, label = 'fitting-original(dropped)', linewidth = 1, color = 'm')
ax.axvline(3.3665176757415685, label = 'fitting-5', linewidth = 1, color = 'g')
ax.axvline(3.279503105590062, label = 'fitting-9', linewidth = 1, color = 'y')
ax.axvline((time[end] + time[start]) / 2, label = 'expect', linestyle = 'dashdot')
ax.axvline((time[end] + time[start]) / 4, linewidth = 1, label = 'expect(-half)', linestyle = 'dashed')
ax.axvline((time[end] + time[start]) * 3 / 4, linewidth = 1, label = 'expect(+half)', linestyle = 'dashed')


ax.axvspan(time[start], time[end], color = "gray", alpha = 0.3, label = 'transit progress')

ax.set_xlabel('time', fontsize = 15)
ax.set_ylabel('flux rate', fontsize = 15)
ax.set_xlim(-0.7, 15)
ax.set_ylim(0.95, 1.03)
ax.grid()
ax.legend()
plt.show()
