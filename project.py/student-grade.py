import matplotlib.pyplot as plt

# 1. Sample Marks Data (File ya direct list se le sakte hain)
marks_list = [85, 92, 45, 78, 62, 88, 35, 95, 73, 68, 54, 81, 90, 42, 77]

# 2. Grade Distribution Categories
grades = {
    'Grade A (90-100)': 0,
    'Grade B (75-89)': 0,
    'Grade C (50-74)': 0,
    'Fail (<50)': 0
}

# 3. Categorizing Marks using simple if/elif/else
for mark in marks_list:
    if mark >= 90:
        grades['Grade A (90-100)'] += 1
    elif mark >= 75:
        grades['Grade B (75-89)'] += 1
    elif mark >= 50:
        grades['Grade C (50-74)'] += 1
    else:
        grades['Fail (<50)'] += 1

# 4. Plotting the Pie Chart
labels = list(grades.keys())
counts = list(grades.values())
colors = ['#4CAF50', '#2196F3', '#FF9800', '#F44336']  # Green, Blue, Orange, Red

plt.figure(figsize=(8, 6))
plt.pie(
    counts, 
    labels=labels, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1}
)

plt.title('🎓 Student Marks & Grade Distribution', fontsize=14, fontweight='bold')
plt.tight_layout()

# show chart
print("📊 Displaying Grade Distribution Pie Chart...")
plt.show()