'''import inheritance_inPython_practice
import ArthmeticOperatorsExercise

def is_power_of(number, base):
  # Base case: when number is smaller than base.
  number = number/base
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return False
  else:
    return True

  # Recursive case: keep dividing number by base.
  return is_power_of(number, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False


for x in range(1, 10, 3):
    print(x)


for x in range(10):
    for y in range(x):
        print(y)'''


def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0]
    return result.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS


def student_grade(name, grade):
	return "{} recieved {}% on the exam".format(name, grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))