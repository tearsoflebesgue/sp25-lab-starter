def get_airspeed_velocity_of(unladen_swallow):
  if unladen_swallow.type == "african":
    return # redacted
  elif unladen_swallow.type == "european":
    return # redacted

# pretend there's code here...

def fizzbuzz(num):
  mul_of_3 = num % 3 == 0 # edit this line
  mul_of_5 = num % 5 == 0 # edit this line
  mul_of_5_and_3 = mul_of_3 and mul_of_5 # edit this line
  if mul_of_5_and_3: # edit this line
    print(f"{num}: fizzbuzz")
  elif mul_of_3: # edit this line
    print(f"{num}: fizz")
  if mul_of_5: # edit this line
    print(f"{num}: buzz")

for i in range(1, 20):
  fizzbuzz(i)

# pretend there's code here...
