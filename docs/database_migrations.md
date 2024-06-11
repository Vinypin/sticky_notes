# Procedures for Performing Django Database Migrations to a Server-Based Relational Database like MariaDB

## Configuring Django to Use MariaDB

1. **Install MariaDB and the necessary Python package**:
   Ensure MariaDB is installed on your server. Install the `mysqlclient` package, which is required for Django to interact with MariaDB.

   
   pip install mysqlclient

 ## Configure the database settings in Django project to use MariaDB.

 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'your_database_host',
        'PORT': 'your_database_port',
    }
}

## Create new migrations based on the changes detected to models.

python manage.py makemigrations

## Apply the migrations to MariaDB database.

python manage.py migrate

# Backup database:
## Always create a backup of database before performing migrations, especially on production systems.

# Use a dedicated database user:
## Create a dedicated database user with the necessary permissions for Django application. This enhances security and makes management easier.

# Test migrations locally:
## Before applying migrations on the production server, test them on a local or staging environment to ensure they work as expected.

# Keep migrations in version control:
## Track migration files in version control (e.g., Git) to keep a history of changes and collaborate with other developers.

# Conclusion

## Migrating a Django project to use MariaDB involves configuring the database settings, creating and applying migrations, and following best practices to ensure a smooth transition. Proper documentation and testing are essential to avoid issues during the migration process.