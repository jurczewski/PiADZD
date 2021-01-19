import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter


def human_format(num, pos):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '%.0f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])

months= pd.read_csv("csv_files/months.csv", parse_dates=["FL_DATE"])
fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(FuncFormatter(human_format))

plt.xticks(fontsize=8, rotation=90)
plt.xlabel('Miesiąc')
plt.ylabel('liczba lotów')
plt.title('Liczba lotów w miesiącach')
plt.xticks(rotation=90)
plt.plot(months.FL_DATE, months.FLIGHTS, '-')
plt.savefig("plots/flights_count_month.png", format="png")
plt.show()
plt.clf()

months2 = pd.read_csv("csv_files/months.csv", parse_dates=["FL_DATE"])
avg_month = months2[months2.FL_DATE!=2020].groupby(months["FL_DATE"].dt.month).mean()
months_no2020 = months2[months2.FL_DATE.dt.year==2020]
avg_month_no2020 = months_no2020.groupby(months["FL_DATE"].dt.month).mean()
plt.xlabel('Miesiąc')
plt.ylabel('liczba lotów')
plt.title('średnia liczba lotów w miesiącach')
plt.bar(avg_month.index, avg_month.FLIGHTS, width=0.3)
plt.savefig("plots/months_avg.png",fromat="png")
plt.title('liczba lotów w 2002 w porównaniu do średniej z lat poprzednich')
plt.bar(avg_month_no2020.index+0.3, avg_month_no2020.FLIGHTS, width=0.3)
plt.legend(labels=['2012-2019', '2020'])
plt.savefig("plots/months_avg_in_2020.png",fromat="png")
plt.show()
plt.clf()


plt.clf()
fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(FuncFormatter(human_format))
quarters = pd.read_csv("csv_files/quarters.csv", parse_dates=["FL_DATE"])
quarters_no2020 = quarters[quarters['FL_DATE'].dt.year!=2020]
avg_quart = quarters.groupby(quarters["FL_DATE"].dt.quarter).mean()
plt.xlabel('Kwartał')
plt.ylabel('liczba lotów')
plt.title('średnia liczba lotów w kwartałach')
plt.bar([1,2,3,4], avg_quart.FLIGHTS)
plt.savefig("plots/quarters_avg.png", format="png")
plt.show()

