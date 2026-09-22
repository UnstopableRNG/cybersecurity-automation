#PY
import csv
import json
import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

VT_API_KEY = os.getenv("VT_API_KEY")
VT_URL = "https://www.virustotal.com/api/v3/files/{}"
HEADERS = {"x-apikey": VT_API_KEY}

input_file = "hashes.csv"
output_file = "report.json"
report_data = []

with open(input_file, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        hash_val = row["SHA256Hash"]
        process_name = row["ProcessName"]
        file_path = row["FilePath"]

        try:
            response = requests.get(VT_URL.format(hash_val), headers=HEADERS)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error scanning {hash_val}: {e}")
            continue     


        if response.status_code == 200:
            json_data = response.json()
            attributes = json_data.get("data", {}).get("attributes", {})
            stats = attributes.get("last_analysis_stats", {})
            malicious = stats.get("malicious", 0)S
            suspicious = stats.get("suspicious", 0)
            harmless = stats.get("harmless", 0)
            undetected = stats.get("undetected", 0)
            threat_label = attributes.get("popular_threat_name")

            result = {
                "ProcessName": process_name,
                "FilePath": file_path,
                "Hash": hash_val,
                "ThreatLabel": threat_label,
                "Detections": {
                    "Malicious": malicious,
                    "Suspicious": suspicious,
                    "Harmless": harmless,
                    "Undetected": undetected
                }
            }
            report_data.append(result)
            print(f"Scanned {process_name} — {malicious} malicious")
        else:
            print(f"Failed to scan {hash_val} — Status: {response.status_code}")

        time.sleep(15)  # Respect rate limit (4 lookups/min)

with open(output_file, "w") as jsonfile:
    json.dump(report_data, jsonfile, indent=2)

print(f"\nReport saved to {output_file}")
