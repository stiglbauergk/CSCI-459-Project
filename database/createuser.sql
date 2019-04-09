# Create the user
create user 'root' identified by 'pass4root';

# Allow it to do anything
grant all privileges on *.* to 'root';
