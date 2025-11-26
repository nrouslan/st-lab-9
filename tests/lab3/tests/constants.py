VALID_CREDENTIALS = [
    ("testuser", "Password123!"),
    ("admin", "AdminPass456!"),
    ("user", "SimplePass789!")
]

INVALID_CREDENTIALS = [
    ("wronguser", "wrongpass"),
    ("testuser", "wrongpassword"),
]

INVALID_CREDENTIALS_WITH_EMPTY_FIELDS = [
    ("", "Password123!"),
    ("testuser", ""),
    ("", "")
]
