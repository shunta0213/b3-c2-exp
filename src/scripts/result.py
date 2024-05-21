import pandas as pd
import scienceplots
import matplotlib.pyplot as plt

plt.style.use(['science', 'ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams["font.size"] = 16

# Load the CSV files
file1 = '../data/-7to7.csv'
file2 = '../data/7to-7.csv'

data1 = pd.read_csv(file1)
data2 = pd.read_csv(file2)

H1 = data1['H/ mT']
R1 = data1[' R /Ω']

H2 = data2['H /mT']
R2 = data2['R /Ω']

plt.figure(figsize=(10, 6))
plt.plot(H1, R1, label='-7 A to 7 A', marker='o')
plt.plot(H2, R2, label='7 A to -7 A', marker='x')
plt.xlabel('Magnetic Field /mT')
plt.ylabel('Resistance / $\\Omega$')
plt.legend()

plt.savefig('../figures/result/result.png')
