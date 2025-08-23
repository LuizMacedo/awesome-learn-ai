#!/usr/bin/env python3
"""
Link validation script for awesome-learn-ai repository.
Validates all Microsoft Learn URLs in README.md and reports broken links.

Usage:
    python scripts/validate_links.py
    python scripts/validate_links.py --output-report broken_links.md
    python scripts/validate_links.py --check-all  # Also check non-Microsoft links
"""

import re
import requests
import time
import argparse
import sys
from pathlib import Path
from urllib.parse import urlparse
from typing import List, Tuple, Dict

class LinkValidator:
    def __init__(self, check_all_links: bool = False):
        self.check_all_links = check_all_links
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; LinkValidatorBot/1.0; +https://github.com/username/awesome-learn-ai)'
        }
    
    def extract_urls_from_markdown(self, file_path: str) -> List[Tuple[str, str, int]]:
        """Extract URLs from markdown file with line numbers."""
        urls = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return []
        
        # Pattern to match markdown links [text](url)
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        
        for line_num, line in enumerate(lines, 1):
            matches = re.findall(link_pattern, line)
            for text, url in matches:
                # Check Microsoft Learn URLs by default, all URLs if check_all_links is True
                if self.check_all_links or 'learn.microsoft.com' in url:
                    # Skip anchor links and relative links
                    if not url.startswith('#') and not url.startswith('./'):
                        urls.append((text, url, line_num))
        
        return urls
    
    def check_url_status(self, url: str) -> Tuple[int, str]:
        """Check URL status and return status code and message. Retries on transient network errors."""
        max_retries = 3
        delay = 2  # seconds
        for attempt in range(1, max_retries + 1):
            try:
                response = requests.get(url, headers=self.headers, timeout=10, allow_redirects=True)
                if response.status_code == 200:
                    return 200, f"OK{' (redirected)' if response.url != url else ''}"
                else:
                    return response.status_code, f"HTTP {response.status_code}"
            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
                if attempt < max_retries:
                    time.sleep(delay)
                    continue
                if isinstance(e, requests.exceptions.Timeout):
                    return -1, "TIMEOUT"
                else:
                    return -2, "CONNECTION_ERROR"
            except requests.exceptions.RequestException as e:
                return -3, f"REQUEST_ERROR: {str(e)}"
            except Exception as e:
                return -4, f"UNKNOWN_ERROR: {str(e)}"
    
    def validate_links(self, file_path: str) -> Dict:
        """Validate all links in the file."""
        print(f"🔍 Validating links in: {file_path}")
        print("=" * 80)
        
        urls = self.extract_urls_from_markdown(file_path)
        
        if not urls:
            link_type = "URLs" if self.check_all_links else "Microsoft Learn URLs"
            print(f"No {link_type} found in the file.")
            return {"total": 0, "working": 0, "broken": 0, "results": []}
        
        results = []
        working_count = 0
        broken_count = 0
        
        for i, (text, url, line_num) in enumerate(urls, 1):
            print(f"[{i}/{len(urls)}] Checking: {url}")
            
            status_code, message = self.check_url_status(url)
            
            if status_code == 200:
                working_count += 1
                status = "✅ WORKING"
                print(f"    Line {line_num}: {status}")
            else:
                broken_count += 1
                status = f"❌ BROKEN ({status_code})"
                print(f"    Line {line_num}: {status} - {message}")
            
            result = {
                "line": line_num,
                "text": text,
                "url": url,
                "status_code": status_code,
                "message": message,
                "working": status_code == 200
            }
            
            results.append(result)
            
            # Add delay to be respectful to the server
            time.sleep(0.5)
        
        print("\n" + "=" * 80)
        print(f"📊 SUMMARY:")
        print(f"   Total URLs checked: {len(urls)}")
        print(f"   ✅ Working URLs: {working_count}")
        print(f"   ❌ Broken URLs: {broken_count}")
        
        return {
            "total": len(urls),
            "working": working_count,
            "broken": broken_count,
            "results": results
        }
    
    def generate_report(self, validation_results: Dict, output_file: str = None):
        """Generate a detailed report of broken links."""
        broken_links = [r for r in validation_results["results"] if not r["working"]]
        
        if not broken_links:
            print("\n🎉 All links are working!")
            return
        
        report = [
            "# 🔗 Link Validation Report",
            f"**Generated:** {time.strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "## 📊 Summary",
            f"- **Total URLs:** {validation_results['total']}",
            f"- **✅ Working:** {validation_results['working']}",
            f"- **❌ Broken:** {validation_results['broken']}",
            "",
            "## ❌ Broken Links",
            ""
        ]
        
        for link in broken_links:
            report.extend([
                f"### 📍 Line {link['line']}: {link['text']}",
                f"- **URL:** `{link['url']}`",
                f"- **Status:** `{link['status_code']}`",
                f"- **Error:** {link['message']}",
                f"- **Action:** Replace with working alternative or remove",
                ""
            ])
        
        report.extend([
            "## 🛠️ Recommended Actions",
            "",
            "1. **Research Alternatives:** Find updated URLs on Microsoft Learn",
            "2. **Update Content:** Replace broken links with working alternatives", 
            "3. **Remove Outdated:** Remove links to deprecated content",
            "4. **Verify Changes:** Re-run validation after updates",
            "",
            "## 🔄 Re-run Validation",
            "",
            "```bash",
            "python scripts/validate_links.py",
            "```"
        ])
        
        report_text = "\n".join(report)
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(report_text)
            print(f"\n📄 Detailed report saved to: {output_file}")
        else:
            print("\n" + "=" * 80)
            print("❌ BROKEN LINKS DETAILS:")
            print("=" * 80)
            for link in broken_links:
                print(f"Line {link['line']}: {link['text']}")
                print(f"  URL: {link['url']}")
                print(f"  Error: {link['status_code']} - {link['message']}")
                print()

def main():
    parser = argparse.ArgumentParser(
        description="Validate links in awesome-learn-ai README.md",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/validate_links.py
  python scripts/validate_links.py --output-report broken_links.md
  python scripts/validate_links.py --check-all
        """
    )
    
    parser.add_argument(
        '--output-report', '-o',
        help='Output detailed report to specified file'
    )
    
    parser.add_argument(
        '--check-all', '-a',
        action='store_true',
        help='Check all links, not just Microsoft Learn URLs'
    )
    
    parser.add_argument(
        '--file', '-f',
        default='README.md',
        help='Markdown file to validate (default: README.md)'
    )
    
    args = parser.parse_args()
    
    # Ensure we're in the right directory
    if not Path(args.file).exists():
        print(f"❌ Error: File '{args.file}' not found.")
        print("💡 Make sure you're running this from the repository root.")
        sys.exit(1)
    
    try:
        validator = LinkValidator(check_all_links=args.check_all)
        results = validator.validate_links(args.file)
        validator.generate_report(results, args.output_report)
        
        # Exit with error code if broken links found
        if results['broken'] > 0:
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\n⏹️  Validation interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()