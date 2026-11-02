user_and_permissions = [('nitin', 'create_movie'),
                        ('mohit', 'book_movie'),
                        ('shyam', 'watch_movie'),
                        ('pillai', 'delete_movie')]

for data in user_and_permissions:
    # tuple unpacking
    user, permission = data
    log_data = f"The user {user} does not have permission {permission}"
    print(log_data)

