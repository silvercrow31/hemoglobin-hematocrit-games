import random

def generate_random_gender():
  """Randomly selects and returns either "male" or "female"."""
  return random.choice(['male', 'female'])

def generate_hemoglobin_value(gender):
  """Generates a random hemoglobin value based on gender and probability."""
  if gender.lower() == 'male':
    normal_lower = 16 - 2
    normal_upper = 16 + 2
  elif gender.lower() == 'female':
    normal_lower = 14 - 2
    normal_upper = 14 + 2
  else:
    print("Invalid gender specified.")
    return None

  probability_of_abnormal = 50  # 50% chance of abnormal value

  if random.randint(1, 100) <= probability_of_abnormal:
    if random.randint(0, 1) == 0:
      return random.randint(normal_lower - 5, normal_lower - 1)
    else:
      return random.randint(normal_upper + 1, normal_upper + 5)
  else:
    return random.randint(normal_lower, normal_upper)

def is_normal_hemoglobin(gender, value):
  """Checks if a hemoglobin value is within the normal range for the gender."""
  if gender.lower() == 'male':
    normal_lower = 16 - 2
    normal_upper = 16 + 2
  elif gender.lower() == 'female':
    normal_lower = 14 - 2
    normal_upper = 14 + 2
  else:
    return False

  return normal_lower <= value <= normal_upper

def main():
  print("Welcome to Hemoglobin Value Trainer!")
  print("Learn to recognize normal and abnormal hemoglobin values.")
  print()

  score = 0
  attempts = 0

  while True:
    gender = generate_random_gender()
    print(f"{gender.capitalize()}")

    value = generate_hemoglobin_value(gender)
    if value is not None:
      print(f"Hb: {value} g/dL")

      while True:
        answer = input("Is this value normal? (y/n): ").strip().lower()
        expected_answer = 'y' if is_normal_hemoglobin(gender, value) else 'n'

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
