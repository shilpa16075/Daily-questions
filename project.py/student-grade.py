import matplotlib.pyplot as plt


def calculate_grades(marks):
    grades = {
        "Grade A (90-100)": 0,
        "Grade B (75-89)": 0,
        "Grade C (50-74)": 0,
        "Fail (<50)": 0,
    }
    for m in marks:
        if m >= 90:
            grades["Grade A (90-100)"] += 1
        elif m >= 75:
            grades["Grade B (75-89)"] += 1
        elif m >= 50:
            grades["Grade C (50-74)"] += 1
        else:
            grades["Fail (<50)"] += 1
    return grades


def show_pie_chart(marks):
    grades = calculate_grades(marks)
    labels = [k for k, v in grades.items() if v > 0]
    counts = [v for v in grades.values() if v > 0]
    pie_colors = ["#2ecc71", "#3498db", "#f39c12", "#e74c3c"]

    plt.figure(figsize=(6, 5))
    plt.pie(counts, labels=labels, autopct="%1.1f%%", colors=pie_colors, startangle=140)
    plt.title("Grade Distribution", fontweight="bold")
    plt.tight_layout()
    plt.show()


def show_bar_chart(marks):
    stats = {
        "Highest": max(marks),
        "Average": sum(marks) / len(marks),
        "Lowest": min(marks),
    }
    bar_colors = ["#2ecc71", "#3498db", "#e74c3c"]  # Green, Blue, Red

    plt.figure(figsize=(7, 5))
    bars = plt.bar(stats.keys(), stats.values(), color=bar_colors, width=0.5)

    # Display exact numbers on top of each bar
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

    plt.title("Key Performance Indicators", fontweight="bold")
    plt.ylabel("Marks")
    plt.ylim(0, 110)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


def show_dashboard(marks):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))

    # Left Side: Pie Chart
    grades = calculate_grades(marks)
    labels = [k for k, v in grades.items() if v > 0]
    counts = [v for v in grades.values() if v > 0]
    pie_colors = ["#2ecc71", "#3498db", "#f39c12", "#e74c3c"]

    ax1.pie(counts, labels=labels, autopct="%1.1f%%", colors=pie_colors, startangle=140)
    ax1.set_title("Grade Share (%)", fontweight="bold")

    # Right Side: Styled Bar Chart (Identical to Option 2)
    stats = {
        "Highest": max(marks),
        "Average": sum(marks) / len(marks),
        "Lowest": min(marks),
    }
    bar_colors = ["#2ecc71", "#3498db", "#e74c3c"]
    bars = ax2.bar(stats.keys(), stats.values(), color=bar_colors, width=0.5)

    for bar in bars:
        yval = bar.get_height()
        ax2.text(
            bar.get_x() + bar.get_width() / 2,
            yval + 1,
            f"{yval:.1f}",
            ha="center",
            va="bottom",
            fontweight="bold",
        )

    ax2.set_title("Key Performance Indicators", fontweight="bold")
    ax2.set_ylim(0, 110)
    ax2.grid(axis="y", linestyle="--", alpha=0.5)

    plt.suptitle("Complete Class Performance Dashboard", fontsize=15, fontweight="bold")
    plt.tight_layout()
    plt.show()


def main():
    marks = [88, 92, 45, 78, 62, 34, 95, 81, 53, 22, 74, 89]

    while True:
        print("\n" + "=" * 45)
        print("  STUDENT MARKS ANALYZER  ")
        print("=" * 45)
        print("1. Display Grade Distribution (Pie Chart)")
        print("2. Display Performance Stats (Bar Chart)")
        print("3. Display Full Dashboard")
        print("4. Enter Custom Marks")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "1":
            show_pie_chart(marks)
        elif choice == "2":
            show_bar_chart(marks)
        elif choice == "3":
            show_dashboard(marks)
        elif choice == "4":
            raw_input = input("\nEnter marks separated by comma: ")
            try:
                new_marks = [float(x.strip()) for x in raw_input.split(",") if x.strip()]
                if new_marks:
                    marks = new_marks
                    print("✅ Marks updated successfully!")
                else:
                    print("❌ No valid numbers entered.")
            except ValueError:
                print("❌ Invalid input! Please enter numbers only.")
        elif choice == "5":
            print("\nExiting program... Thank you!")
            break
        else:
            print("❌ Invalid choice! Try again.")


if __name__ == "__main__":
    main()