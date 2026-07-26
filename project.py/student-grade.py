import matplotlib.pyplot as plt


def calculate_grades(marks_list):
    grades = {"Grade A (90-100)": 0, "Grade B (75-89)": 0, "Grade C (50-74)": 0, "Fail (<50)": 0}

    for mark in marks_list:
        if mark >= 90:
            grades["Grade A (90-100)"] += 1
        elif mark >= 75:
            grades["Grade B (75-89)"] += 1
        elif mark >= 50:
            grades["Grade C (50-74)"] += 1
        else:
            grades["Fail (<50)"] += 1

    return grades


def plot_grade_distribution(marks_list):
    grades = calculate_grades(marks_list)
    labels = list(grades.keys())
    counts = list(grades.values())
    colors = ["#4CAF50", "#2196F3", "#FF9800", "#F44336"]

    # Filter out categories with 0 count to keep chart clean
    active_labels = [label for label, count in zip(labels, counts) if count > 0]
    active_counts = [count for count in counts if count > 0]
    active_colors = [color for color, count in zip(colors, counts) if count > 0]

    plt.figure(figsize=(7, 7))
    plt.pie(
        active_counts,
        labels=active_labels,
        autopct="%1.1f%%",
        startangle=140,
        colors=active_colors,
        explode=[0.05] * len(active_counts),
    )
    plt.title("Student Grade Distribution Pie Chart", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()


def plot_max_min_avg(marks_list):
    max_mark = max(marks_list)
    min_mark = min(marks_list)
    avg_mark = sum(marks_list) / len(marks_list)

    categories = ["Highest Mark", "Average Mark", "Lowest Mark"]
    values = [max_mark, avg_mark, min_mark]
    bar_colors = ["#2ecc71", "#3498db", "#e74c3C"]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(categories, values, color=bar_colors, width=0.5)

    # Adding values on top of bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval + 1,
            f"{yval:.1f}",
            ha="center",
            va="bottom",
            fontweight="bold",
        )

    plt.title("Performance Summary (Max, Min & Average)", fontsize=14, fontweight="bold")
    plt.ylabel("Marks")
    plt.ylim(0, 110)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()


def main():
    # Sample dataset of student marks
    student_marks = [88, 92, 45, 78, 62, 34, 95, 81, 53, 22, 74, 89]

    while True:
        print("\n" + "=" * 45)
        print(" STUDENT MARKS & GRADE ANALYZER ")
        print("=" * 45)
        print("1. Display Grade Distribution (Pie Chart)")
        print("2. Display Highest, Lowest & Average Marks (Bar Chart)")
        print("3. Exit Program")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            print("\nGenerating Grade Distribution Pie Chart...")
            plot_grade_distribution(student_marks)
        elif choice == "2":
            print("\nGenerating Max/Min/Average Comparison Bar Chart...")
            plot_max_min_avg(student_marks)
        elif choice == "3":
            print("\nExiting Program. Thank you!")
            break
        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()