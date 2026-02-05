from tables import create_tables
from services import create_user, create_post, get_user_by_id, get_all_users, get_posts_by_user, delete_post, update_user_email

# Create Tables
create_tables()

# Create Data
create_user("sonam", "sonam@example.com")
create_user("raj", "raj@example.com")
create_post(1, "Hello World", "This is Sonam's first post")
create_post(2, " Post 2", "Hi from Raj Malhotra!")

#Read data
print(get_user_by_id(2))
print(get_all_users())
print(get_posts_by_user(1))

#Update data
update_user_email(1, "sonam@newdomain.com")

# Delete Data
delete_post(2)