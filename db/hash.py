from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()



# Password hashing
def hash_password(password: str) -> str:
    """Hash a plain password"""
    return pwd_context.hash(password)

# Password varification
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hashed password"""
    return pwd_context.verify(plain_password, hashed_password) 