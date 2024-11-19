import os

from app.services.utils.passwordgenerator import PasswordGenerator

# Create an instance of PasswordUtils with the salt from the environment
PASSWORD_SALT = os.getenv("PASSWORD_SALT")
if not PASSWORD_SALT:
    raise EnvironmentError("PASSWORD_SALT environment variable is not set")

password_utils_instance = PasswordGenerator(PASSWORD_SALT)


def get_password_generator() -> PasswordGenerator:
    """Return the PasswordUtils instance."""
    return password_utils_instance
