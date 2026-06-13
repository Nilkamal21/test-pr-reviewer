def get_user_profile(user_id):
    # INSECURE: Direct string concatenation allows for SQL Injection!
    query = "SELECT * FROM profiles WHERE id = '" + user_id + "'"
    print(f"Executing database search lookup: {query}")
    return query
