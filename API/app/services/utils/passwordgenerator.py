from passlib.context import CryptContext


class PasswordGenerator:
    salt: str

    def __init__(self, salt):
        if not salt:
            raise ValueError("Salt can not be empty")
        self.salt = salt
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, password: str) -> str:
        """Hash a password with a salt."""
        salted_password = f"{password}{self.salt}"
        return self.pwd_context.hash(salted_password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a plain password against a hashed password."""
        salted_password = f"{plain_password}{self.salt}"
        return self.pwd_context.verify(salted_password, hashed_password)
