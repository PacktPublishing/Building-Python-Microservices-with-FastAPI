
from datetime import datetime

def audit_log_transaction(touristId: str, message=""):
    with open("audit_log.txt", mode="a") as logfile:
        content = f"tourist {touristId} executed {message} at {datetime.now()}"
        logfile.write(content)


