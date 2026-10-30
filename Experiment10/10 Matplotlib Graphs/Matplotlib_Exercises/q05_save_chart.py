from pathlib import Path
import matplotlib.pyplot as plt

weeks = ["Week 1", "Week 2", "Week 3", "Week 4"]
attendance = [32, 35, 31, 38]

figure, axis = plt.subplots(figsize=(7, 4))
axis.plot(weeks, attendance, marker="s", linewidth=2, color="teal", label="Attendance")
axis.set_title("Weekly Class Attendance")
axis.set_xlabel("Week")
axis.set_ylabel("Students present")
axis.set_ylim(0, 45)
axis.grid(True, linestyle="--", alpha=0.4)
axis.legend()
figure.tight_layout()
figure.savefig(Path(__file__).with_name("weekly_attendance.png"), dpi=150)
plt.show()
