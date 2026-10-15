server_ip = (192, 168, 1, 10)
allowed_ips = ["192.168.1.1", "192.168.1.2"]

def update_allowed_ips():
    n = int(input("Enter number of allowed IP addresses: "))
    allowed_ips.clear()

    for i in range(n):
        ip = input("Enter allowed IP address: ")
        allowed_ips.append(ip)

    print("Allowed IPs updated successfully.")

def update_server_ip():
    print("Server IP cannot be changed.")

def display_config():
    print("Server IP:", server_ip)
    print("Allowed IPs:", allowed_ips)

while True:
    print("\n1. Update Allowed IPs")
    print("2. Update Server IP")
    print("3. Display Configuration")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        update_allowed_ips()
    elif choice == "2":
        update_server_ip()
    elif choice == "3":
        display_config()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")