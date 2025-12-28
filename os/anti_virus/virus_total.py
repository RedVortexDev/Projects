import os
from dataclasses import dataclass

import vt

@dataclass
class ScanResults:
    malicious: int
    suspicious: int
    undetected: int
    harmless: int

class VirusTotal:
    def __init__(self, file_name):
        self.file_name = file_name
        self.client = vt.Client(str(os.getenv('VIRUS_TOTAL_API_KEY')))

    def scan(self) -> ScanResults:
        try:
            with open(self.file_name, 'rb') as file:
                analysis = self.client.scan_file(file, wait_for_completion=True).to_dict()
                stats = analysis['attributes']['stats']
                return ScanResults(
                    malicious=stats.get('malicious', 0),
                    suspicious=stats.get('suspicious', 0),
                    undetected=stats.get('undetected', 0),
                    harmless=stats.get('harmless', 0)
                )
        finally:
            self.client.close()