import os

def login_user(username, password):
    # 1. HARDCODED PASSWORD (Our security scanner should catch this!)
    db_password = "super_secret_admin_password_123"

    # 2. DANGEROUS EVAL STATEMENT (Our security scanner should catch this too!)
    eval(username)

    print(f"Logging in {username}...")
