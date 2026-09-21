import json
from datetime import datetime
from pathlib import Path

def save_report(results):

    Path("reports").mkdir(exist_ok=True)

    report = []

    for r in results:

        report.append({
            "name": r.name,
            "success": r.success,
            "duration": r.duration,
            "message": r.message
        })

    filename = f"reports/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w") as f:
        json.dump(report, f, indent=2)

    return filename