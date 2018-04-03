# Start with users that need to be verified, and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    user = unconfirmed_users.pop()

    print("Verifying users: " + user.title())
    confirmed_users.append(user)

# Display all confirmed users.
print("\nThe following users have been confirmed: ")
for user in confirmed_users:
    print(user.title())
