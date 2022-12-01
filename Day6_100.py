#LOGIN PAGE
print("Secure Login")
username = input("What is your user_name? ")
password = input("What is your password? ")

if username == "abhiram" and password == "abhiram@123":
  print("Welcome, abhiram! You are looking nice today!")
elif username == "satish" and password == "satish@123":
  print("Hi satish! Love your hair today!")
elif username == "nikhil" and password == "nikhil@123":
  print("Yo! nikhil! What up?!")
else:
  print("You do not have access. Go away!")
