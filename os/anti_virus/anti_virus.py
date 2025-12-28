import sys

import consts
from virus_total import VirusTotal

if __name__ == "__main__":
    consts.init()

    scanner = VirusTotal(sys.argv[1])
    results = scanner.scan()
    print("# Scan Results:")
    print(f"Malicious: {results.malicious}")
    print(f"Suspicious: {results.suspicious}")
    print(f"Undetected: {results.undetected}")
    print(f"Harmless: {results.harmless}")
