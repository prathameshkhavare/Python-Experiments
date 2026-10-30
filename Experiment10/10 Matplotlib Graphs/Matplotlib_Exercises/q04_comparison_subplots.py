import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
revenue = [18, 22, 20, 28, 33]
orders = [120, 145, 138, 176, 205]

figure, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].plot(months, revenue, marker="o", color="royalblue")
axes[0].set_title("Monthly Revenue")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Revenue (thousands)")
axes[0].grid(True, alpha=0.3)
axes[1].bar(months, orders, color="seagreen")
axes[1].set_title("Monthly Orders")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Orders")
figure.suptitle("Business Performance")
figure.tight_layout()
plt.show()
