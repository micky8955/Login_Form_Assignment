users = {
  "ahad" : "123",
  "admin" : "admin123",
  "test" : "testpass"
}

print("===== Login System =====")

username = input("Enter your username: ")
password = input("Enter your password: ")

if username in users and users[username] == password:
  print("\nLogin successful! Welcome,", username)

else:
   print("\nInvalid username or password. Please try again.")
