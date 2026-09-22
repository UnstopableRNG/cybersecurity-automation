# Cybersecurity Automation

A cybersecurity automation project developed as part of my studies in Digital Forensics and Cyber Security at TU Dublin.

## Overview

This project combines PowerShell and Python to automate a basic process-analysis and threat-intelligence workflow on a Windows system.

The PowerShell component collects information about running processes and calculates SHA-256 hashes for accessible executable files.

The Python component reads the generated hashes and queries the VirusTotal API to obtain threat-intelligence information. The results are then saved as a structured JSON report.

## Workflow

```text
Windows Processes
       |
       v
PowerShell
       |
       | Collect process name,
       | PID, file path and SHA-256 hash
       v
hashes.csv
       |
       v
Python
       |
       | Query VirusTotal API
       v
report.json
```

## Technologies

- Python
- PowerShell
- Windows
- VirusTotal API
- CSV
- JSON
- SHA-256
- Python Requests
- python-dotenv

## Project Components

### PowerShell Process Collection

`Get-ProcessHashes.ps1`

The PowerShell script:

1. Retrieves running processes using `Get-Process`.
2. Attempts to obtain the executable path for each process.
3. Calculates a SHA-256 hash using `Get-FileHash`.
4. Stores the process name, process ID, file path and hash.
5. Exports the results to `hashes.csv`.

Processes that cannot be accessed are skipped.

### Python Threat Intelligence Analysis

`vt_hash_checker.py`

The Python script:

1. Loads the VirusTotal API key from an environment variable.
2. Reads SHA-256 hashes from `hashes.csv`.
3. Queries the VirusTotal API for each hash.
4. Extracts the available analysis statistics.
5. Records the threat label when available.
6. Produces a structured `report.json` file.

The script also includes a delay between API requests to respect the VirusTotal API rate limit used by the project.

## Input and Output

### `hashes.csv`

Contains information collected from running processes, including:

- Process name
- Process ID
- File path
- SHA-256 hash

### `report.json`

Contains the results returned from the VirusTotal analysis, including:

- Process name
- File path
- SHA-256 hash
- Threat label
- Malicious detections
- Suspicious detections
- Harmless detections
- Undetected results

## Setup

### Requirements

Python 3 and PowerShell are required.

Install the Python dependencies:

```bash
pip install requests python-dotenv
```

Create a `.env` file in the project directory:

```text
VT_API_KEY=your_api_key_here
```

Do not upload your real API key to GitHub.

## Usage

### 1. Collect process hashes

Run the PowerShell script:

```powershell
.\Get-ProcessHashes.ps1
```

This generates:

```text
hashes.csv
```

### 2. Run the Python analysis

Run:

```bash
python vt_hash_checker.py
```

The results are written to:

```text
report.json
```

## Example Workflow

The project can be used to collect hashes from active Windows processes and then submit those hashes to VirusTotal for additional threat-intelligence information.

The resulting JSON report can be used as structured output for further analysis.

## Project Files

| File | Description |
|---|---|
| `Get-ProcessHashes.ps1` | PowerShell process and SHA-256 hash collection script |
| `vt_hash_checker.py` | Python VirusTotal analysis script |
| `hashes.csv` | Example process and hash data |
| `report.json` | Example VirusTotal analysis output |
| `requirements.txt` | Python package requirements |

## Learning Outcomes

This project provided practical experience with:

- Python scripting
- PowerShell scripting
- File handling
- CSV processing
- JSON processing
- SHA-256 hashing
- REST API interaction
- Environment variables
- Cybersecurity automation
- Threat-intelligence workflows

## Notes

This project is intended for educational and defensive cybersecurity purposes.

The included `hashes.csv` and `report.json` files are example outputs generated during the project.

API keys and other credentials should never be committed to the repository.
