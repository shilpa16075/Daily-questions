import csv
import os
import pandas as pd
import matplotlib.pyplot as plt

# CSV Storage File Configuration
DATA_FILE = "study_data.csv"

def initialize_file():
    """Checks if CSV exists; if not, creates it with proper headers."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Subject", "Hours", "Focus_Type"])
        print(f"📁 Created new storage file: {DATA_FILE}")
    else:
        print(f"📁 Existing storage file loaded: {DATA_FILE}")

# Initialize the setup on script start
if __name__ == "__main__":
    initialize_file()
    import csv
import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "study_data.csv"

# --- STEP 2: File Initialization ---
def initialize_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Subject", "Hours", "Focus_Type"])

# --- STEP 3: Core Functions ---

def log_study_session():
    """User se entry lekar CSV me store karta hai."""
    print("\n--- 📝 Log New Study Session ---")
    date = input("Enter Date (YYYY-MM-DD) [Leave blank for Today]: ").strip()
    if not date:
        date = pd.Timestamp.now().strftime('%Y-%m-%d')

    subject = input("Enter Subject (e.g., Python, MySQL, Git): ").strip().title()
    
    try:
        hours = float(input("Enter Hours Spent (e.g., 2.5): "))
    except ValueError:
        print("❌ Invalid hours entered! Please enter a number.")
        return

    print("\nSelect Focus Type:")
    print("1. Deep Focus 🎯")
    print("2. Short Break ☕")
    print("3. Distraction 📱")
    choice = input("Enter choice (1-3): ").strip()

    focus_map = {"1": "Deep Focus", "2": "Short Break", "3": "Distraction"}
    focus_type = focus_map.get(choice, "Deep Focus")

    # Save to CSV
    with open(DATA_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([date, subject, hours, focus_type])

    print(f"\n✅ Session logged successfully for {subject} ({hours} hrs)!")


def show_dashboard():
    """CSV se data read karke Bar Chart aur Pie Chart render karta hai."""
    if not os.path.exists(DATA_FILE) or os.stat(DATA_FILE).st_size == 0:
        print("\n❌ No data found! Please log a session first.")
        return

    df = pd.read_csv(DATA_FILE)

    if df.empty:
        print("\n❌ Storage file is empty. Log some data first!")
        return

    # Dashboard Plot Layout (1 Row, 2 Subplots)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle('🎓 Study & Productivity Dashboard', fontsize=15, fontweight='bold')

    # Chart 1: Bar Chart (Subject vs Total Hours)
    subject_data = df.groupby('Subject')['Hours'].sum()
    bars = ax1.bar(subject_data.index, subject_data.values, color='#2563EB', edgecolor='black')
    ax1.set_title('Total Hours Spent per Subject', fontweight='bold')
    ax1.set_ylabel('Hours Spent')
    plt.sca(ax1)
    plt.xticks(rotation=20)

    # Values print on top of each bar
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, yval + 0.05, f'{yval:.1f}h', ha='center', va='bottom')

    # Chart 2: Pie Chart (Focus Ratio)
    focus_data = df.groupby('Focus_Type')['Hours'].sum()
    color_map = {'Deep Focus': '#10B981', 'Short Break': '#F59E0B', 'Distraction': '#EF4444'}
    colors = [color_map.get(ft, '#9CA3AF') for ft in focus_data.index]

    ax2.pie(
        focus_data.values, 
        labels=focus_data.index, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=colors,
        wedgeprops={'edgecolor': 'black', 'linewidth': 1}
    )
    ax2.set_title('Productivity & Focus Breakdown', fontweight='bold')

    plt.tight_layout()
    print("\n📊 Loading Visual Dashboard Window...")
    plt.show()


def main_menu():
    """Main CLI Execution Loop."""
    initialize_file()
    
    while True:
        print("\n==============================")
        print("  📚 STUDY & HABIT TRACKER  ")
        print("==============================")
        print("1. Log Study Session")
        print("2. View Dashboard (Bar & Pie Charts)")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ").strip()

        if choice == '1':
            log_study_session()
        elif choice == '2':
            show_dashboard()
        elif choice == '3':
            print("\nExiting Tracker. Happy Learning! 👋")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()