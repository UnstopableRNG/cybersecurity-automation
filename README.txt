Malicious Process Analyzer

This tool identifies potentially malicious running processes on a Windows machine by:
1. Collecting SHA-256 hashes of active processes
2. Scanning those hashes against the VirusTotal API


Files
- Get-ProcessHashes.ps1 — PowerShell script to collect process hashes
- vt_hash_checker.py — Python script to scan hashes via VirusTotal
- .env — Store your VirusTotal API key


Setup
1. Install Python packages:
pip install requests python-dotenv
2. Create a `.env` file in the same folder with your API key:
VT_API_KEY=your_api_key_here


Usage
1. Run the PowerShell script to generate hashes.csv:
.\Get-ProcessHashes.ps1
2. Then run the Python script to analyze the hashes:
python vt_hash_checker.py
The output report will be saved as 'report.json' in the same folder.


Output Files
- hashes.csv — Contains process names, IDs, file paths, and SHA-256 hashes
- report.json — VirusTotal scan results for each hash
