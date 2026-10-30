import matplotlib.pyplot as plt

subjects = ["Maths", "Science", "English", "History", "Computing"]
marks = [88, 76, 91, 72, 95]
colors = ["royalblue", "seagreen", "darkorange", "mediumpurple", "teal"]

plt.bar(subjects, marks, color=colors)
plt.title("Student Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.35)
plt.tight_layout()
plt.show()
