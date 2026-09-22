# Cybersecurity Automation

A cybersecurity scripting project developed as part of my studies in Digital Forensics and Cyber Security at TU Dublin.

## Overview

This project combines Python and PowerShell to automate a cybersecurity workflow.

The PowerShell component is used to collect system information, while the Python component processes the collected data and produces security-related output.

## Technologies

- Python
- PowerShell
- Windows
- Cybersecurity scripting
- Threat intelligence API

## Project Components

### Python

`vt_hash_checker.py`

The Python component processes file hashes and uses a threat intelligence service to check the hashes.

### PowerShell

`Get-ProcessHashes.ps1`

The PowerShell component is used to collect process information and generate hashes that can be passed into the Python workflow.

### Supporting Files

- `hashes.csv` — sample hash data
- `report.json` — structured output from the workflow
- `README.txt` — original project documentation

## Workflow

```text
PowerShell
    |
    v
Collect process information
    |
    v
Generate hashes
    |
    v
hashes.csv
    |
    v
Python
    |
    v
Threat intelligence lookup
    |
    v
report.json
