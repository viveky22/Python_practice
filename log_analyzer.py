import json

def analyze_logs(file):
    with open(file, 'r') as f:
        data = json.load(f)
    
    error_count = 0
    errors = []
    for entry in data:
        if entry["level"] == "ERROR":
            error_count += 1
  
            errors.append(entry)

    return error_count, errors


count, error_logs = analyze_logs("logs.json")

print("Total Errors:", count)
print("Error Details:")

for e in error_logs:
    print(e)