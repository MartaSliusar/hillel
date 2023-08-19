results: list[str] = []

with open("rockyou.txt", "r") as file:
    for line in file:
        line: str = line.strip()
        if "user" in line:
            print("Line:", line)
            user_input = input("Do you wanna add line?(yes/no):").upper()

            if user_input == "YES":
                results.append(line)

print("Results:", results)
print("Number:", len(results))
