from src.planner import plan_learning

output = plan_learning("SQL Window Functions")
for key, value in output.items():
    print(f"\n--- {key.upper()} ---\n{value}\n")
