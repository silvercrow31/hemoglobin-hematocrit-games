import random

def generate_random_gender():
    # Randomly select a gender (male or female)
    return random.choice(['male', 'female'])

def generate_hematocrite_value(gender):
    if gender.lower() == 'male':
        # Hematocrite range for males: 47 +/- 7
        normal_lower = 47 - 7
        normal_upper = 47 + 7
    elif gender.lower() == 'female':
        # Hematocrite range for females: 42 +/- 2
        normal_lower = 42 - 5
        normal_upper = 42 + 5
    else:
        print("Invalid gender specified.")
        return None
    
    # Define the probability (in percentage) of generating an abnormal value
    probability_of_abnormal = 50  # 50% chance of abnormal value

    if random.randint(1, 100) <= probability_of_abnormal:
        # Generate an abnormal value
        if random.randint(0, 1) == 0:
            # Generate a value lower than the normal range
            return random.randint(normal_lower - 10, normal_lower - 1)
        else:
            # Generate a value higher than the normal range
            return random.randint(normal_upper + 1, normal_upper + 10)
    else:
        # Generate a normal value within the specified range
        return random.randint(normal_lower, normal_upper)

def is_normal_hematocrite(gender, value):
    if gender.lower() == 'male':
        normal_lower = 47 - 7
        normal_upper = 47 + 7
    elif gender.lower() == 'female':
        normal_lower = 42 - 5
        normal_upper = 42 + 5
    else:
        return False  # Invalid gender
    
    return normal_lower <= value <= normal_upper

def main():
    print("Welcome to Hematocrit Value Trainer!")
    print("Learn to recognize normal and abnormal hematocrit values.")
    print()

    score = 0
    attempts = 0

    while True:
        # Randomly assign a gender
        gender = generate_random_gender()
        print(f"{gender.capitalize()}")

        # Generate a hematocrit value based on the assigned gender
        value = generate_hematocrite_value(gender)
        if value is not None:
            print(f"HTO: {value}")

            while True:
                answer = input("Is this value normal? (y/n): ").strip().lower()
                expected_answer = 'y' if is_normal_hematocrite(gender, value) else 'n'

                if answer in ['y', 'n']:
                    if answer == expected_answer:
                        print("Correct! This value is NORMAL." if answer == 'y' else "Correct! This value is NOT NORMAL.")
                        score += 1
                    else:
                        print("Incorrect. This value is NORMAL." if expected_answer == 'y' else "Incorrect. This value is NOT NORMAL.")
                    attempts += 1
                    break
                else:
                    print("Invalid response. Please enter 'y' or 'n'.")

            print(f"SCORE: {score} / {attempts} attempts\n") 

if __name__ == "__main__":
    main()
