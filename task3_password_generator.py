"""CodSoft Task 3 - Password Generator (length + complexity)."""
import secrets
import string


def ask_yes_no(prompt):
    return input(prompt).strip().lower() in ("y", "yes")


def generate_password(length, use_upper, use_digits, use_symbols):
    pools = [string.ascii_lowercase]
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append("!@#$%^&*()-_=+[]{};:,.?")

    # Guarantee at least one character from every chosen pool
    chars = [secrets.choice(pool) for pool in pools]
    all_chars = "".join(pools)
    chars += [secrets.choice(all_chars) for _ in range(length - len(chars))]
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def main():
    print("=== PASSWORD GENERATOR ===")
    while True:
        try:
            length = int(input("Desired password length (min 4): "))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if length < 4:
            print("Length must be at least 4.")
            continue

        print("\nChoose complexity:")
        use_upper = ask_yes_no("Include uppercase letters? (y/n): ")
        use_digits = ask_yes_no("Include digits? (y/n): ")
        use_symbols = ask_yes_no("Include symbols? (y/n): ")

        password = generate_password(length, use_upper, use_digits, use_symbols)
        print(f"\nGenerated password: {password}")

        if not ask_yes_no("\nGenerate another? (y/n): "):
            print("Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()
