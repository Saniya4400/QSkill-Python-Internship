import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
data = pd.read_csv("data.csv")

# Print data
print(data)

# -------- BAR CHART --------
plt.bar(data['Name'], data['Marks'])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Marks of Students")
plt.show()

# -------- SCATTER PLOT --------
plt.scatter(data['Attendance'], data['Marks'])
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.title("Attendance vs Marks")
plt.show()


# -------- HEATMAP --------
plt.figure()
sns.heatmap(data.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()
