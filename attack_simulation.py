# attack_simulation.py

# Simulating a basic SQL Injection attack attempt.
def simulate_sql_injection():
    payload = "' OR 1=1 --"
    print(f"Simulating SQL Injection attack with payload: {payload}")
    # Normally, you would inject this into a vulnerable SQL query.
    return payload

simulate_sql_injection()
