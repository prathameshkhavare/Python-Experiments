import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [42, 50, 55, 64, 68, 77, 83, 91]

plt.scatter(study_hours, marks, color="darkorange", marker="o", label="Students")
plt.title("Study Hours and Exam Marks")
plt.xlabel("Study hours")
plt.ylabel("Exam marks")
plt.xticks(study_hours)
plt.grid(True, linestyle="--", alpha=0.4)
plt.legend()
plt.tight_layout()
plt.show()
