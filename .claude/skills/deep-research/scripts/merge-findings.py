#!/usr/bin/env python3
"""
Merge Research Findings Script

Merges findings from multiple search result files into a consolidated view.
Helps identify:
- Duplicate information across sources
- Conflicting claims
- Consensus patterns
- Gaps in coverage

Usage: python merge-findings.py <session-path> [--output merged-findings.md]
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Set, Any
from collections import defaultdict
import argparse


class FindingsMerger:
    def __init__(self, session_path: str):
        self.session_path = Path(session_path)
        self.findings: List[Dict[str, Any]] = []
        self.sources: Dict[str, List[str]] = defaultdict(list)
        self.topics: Dict[str, List[Dict]] = defaultdict(list)
        self.urls: Set[str] = set()
    
    def merge(self) -> str:
        """Merge all findings and return markdown report"""
        
        print(f"Merging findings from: {self.session_path}")
        
        # Collect from search results
        self._collect_search_results()
        
        # Collect from deep dives
        self._collect_deep_dives()
        
        # Analyze and merge
        self._analyze_findings()
        
        # Generate merged report
        return self._generate_report()
    
    def _collect_search_results(self):
        """Extract findings from search result files"""
        results_dir = self.session_path / "01-search-results"
        
        if not results_dir.exists():
            print("Warning: No search results directory found")
            return
        
        for result_file in results_dir.glob("*.md"):
            if result_file.name == "coverage-matrix.md":
                continue
            
            print(f"  Processing: {result_file.name}")
            content = result_file.read_text(encoding='utf-8')
            
            # Extract source name from filename
            source_name = result_file.stem
            
            # Extract results sections
            results = self._extract_results(content, source_name)
            self.findings.extend(results)
    
    def _collect_deep_dives(self):
        """Extract findings from deep dive files"""
        deep_dives_dir = self.session_path / "02-deep-dives"
        
        if not deep_dives_dir.exists():
            return
        
        for dive_file in deep_dives_dir.glob("*.md"):
            print(f"  Processing deep dive: {dive_file.name}")
            content = dive_file.read_text(encoding='utf-8')
            
            source_name = f"deep-dive:{dive_file.stem}"
            
            # Extract key findings
            findings = self._extract_deep_dive_findings(content, source_name)
            self.findings.extend(findings)
    
    def _extract_results(self, content: str, source: str) -> List[Dict]:
        """Extract individual results from a search results file"""
        findings = []
        
        # Match result blocks (### Result N: Title pattern)
        result_pattern = r'### (?:Result\s*\d+[:\s]+)?(.+?)(?=###|\Z)'
        matches = re.findall(result_pattern, content, re.DOTALL)
        
        for match in matches:
            finding = self._parse_result_block(match, source)
            if finding:
                findings.append(finding)
        
        return findings
    
    def _parse_result_block(self, block: str, source: str) -> Dict:
        """Parse a single result block into structured data"""
        finding = {
            'source': source,
            'title': '',
            'url': '',
            'relevance': 'unknown',
            'excerpts': [],
            'topics': [],
            'raw': block[:500]  # First 500 chars for reference
        }
        
        # Extract title (first line)
        lines = block.strip().split('\n')
        if lines:
            finding['title'] = lines[0].strip()
        
        # Extract URL
        url_match = re.search(r'\*\*URL\*\*:\s*(\S+)', block)
        if url_match:
            finding['url'] = url_match.group(1)
            self.urls.add(finding['url'])
        
        # Extract relevance
        rel_match = re.search(r'\*\*Relevance\*\*:\s*(\d+|high|medium|low)', block, re.IGNORECASE)
        if rel_match:
            finding['relevance'] = rel_match.group(1).lower()
        
        # Extract excerpts (quoted text)
        excerpts = re.findall(r'>\s*(.+)', block)
        finding['excerpts'] = excerpts[:3]  # Keep top 3
        
        # Identify topics (simple keyword extraction)
        finding['topics'] = self._extract_topics(block)
        
        return finding if finding['title'] else None
    
    def _extract_deep_dive_findings(self, content: str, source: str) -> List[Dict]:
        """Extract findings from deep dive format"""
        findings = []
        
        # Look for Key Findings section
        findings_match = re.search(r'## Key (?:Findings|Takeaways)(.+?)(?=##|\Z)', content, re.DOTALL | re.IGNORECASE)
        
        if findings_match:
            section = findings_match.group(1)
            # Extract numbered or bulleted items
            items = re.findall(r'^\s*(?:\d+\.|[-*])\s*(.+)', section, re.MULTILINE)
            
            for item in items:
                findings.append({
                    'source': source,
                    'title': item[:100],
                    'url': '',
                    'relevance': 'high',  # Deep dives are presumably high relevance
                    'excerpts': [item],
                    'topics': self._extract_topics(item),
                    'raw': item
                })
        
        return findings
    
    def _extract_topics(self, text: str) -> List[str]:
        """Extract topic keywords from text"""
        # Common technical terms to look for
        tech_terms = [
            'rag', 'llm', 'embedding', 'vector', 'chunk', 'retrieval',
            'architecture', 'implementation', 'performance', 'latency',
            'accuracy', 'benchmark', 'production', 'scalability',
            'api', 'model', 'training', 'inference', 'fine-tuning'
        ]
        
        text_lower = text.lower()
        found = [term for term in tech_terms if term in text_lower]
        
        return found
    
    def _analyze_findings(self):
        """Analyze findings for patterns, duplicates, conflicts"""
        
        # Group by URL (exact duplicates)
        url_groups = defaultdict(list)
        for finding in self.findings:
            if finding['url']:
                url_groups[finding['url']].append(finding)
        
        # Group by topic
        for finding in self.findings:
            for topic in finding['topics']:
                self.topics[topic].append(finding)
        
        # Track sources per finding
        for finding in self.findings:
            self.sources[finding['title'][:50]].append(finding['source'])
    
    def _generate_report(self) -> str:
        """Generate merged findings report"""
        
        timestamp = datetime.now().isoformat()
        
        report = f"""# Merged Research Findings

**Generated**: {timestamp}
**Session**: {self.session_path}
**Total Findings**: {len(self.findings)}
**Unique URLs**: {len(self.urls)}

---

## Summary Statistics

- **Findings from search results**: {len([f for f in self.findings if 'deep-dive' not in f['source']])}
- **Findings from deep dives**: {len([f for f in self.findings if 'deep-dive' in f['source']])}
- **Topics identified**: {len(self.topics)}

---

## Findings by Topic

"""
        # Sort topics by number of findings
        sorted_topics = sorted(self.topics.items(), key=lambda x: len(x[1]), reverse=True)
        
        for topic, topic_findings in sorted_topics[:10]:  # Top 10 topics
            report += f"\n### {topic.upper()} ({len(topic_findings)} findings)\n\n"
            
            # Show top 5 findings for this topic
            high_rel = [f for f in topic_findings if f['relevance'] in ['high', '5', '4']]
            to_show = (high_rel or topic_findings)[:5]
            
            for finding in to_show:
                report += f"- **{finding['title'][:80]}**\n"
                report += f"  - Source: {finding['source']}\n"
                if finding['url']:
                    report += f"  - URL: {finding['url']}\n"
                if finding['excerpts']:
                    report += f"  - Key: \"{finding['excerpts'][0][:100]}...\"\n"
                report += "\n"

        report += """---

## Potential Duplicates

*Findings from multiple sources covering the same URL:*

"""
        # Find duplicates
        url_groups = defaultdict(list)
        for finding in self.findings:
            if finding['url']:
                url_groups[finding['url']].append(finding['source'])
        
        duplicates = {url: sources for url, sources in url_groups.items() if len(sources) > 1}
        
        if duplicates:
            for url, sources in list(duplicates.items())[:10]:
                report += f"- {url}\n"
                report += f"  - Found in: {', '.join(sources)}\n"
        else:
            report += "*No duplicates found*\n"

        report += """
---

## High Relevance Findings

*Findings marked as high relevance:*

"""
        high_rel = [f for f in self.findings if f['relevance'] in ['high', '5', '4']]
        
        for finding in high_rel[:15]:
            report += f"### {finding['title'][:80]}\n"
            report += f"- **Source**: {finding['source']}\n"
            if finding['url']:
                report += f"- **URL**: {finding['url']}\n"
            report += f"- **Topics**: {', '.join(finding['topics']) or 'N/A'}\n"
            if finding['excerpts']:
                report += f"- **Key excerpt**:\n  > {finding['excerpts'][0][:200]}\n"
            report += "\n"

        report += """---

## Source Coverage

*Findings per source:*

| Source | Findings | High Relevance |
|--------|----------|----------------|
"""
        source_counts = defaultdict(lambda: {'total': 0, 'high': 0})
        for finding in self.findings:
            source_counts[finding['source']]['total'] += 1
            if finding['relevance'] in ['high', '5', '4']:
                source_counts[finding['source']]['high'] += 1
        
        for source, counts in sorted(source_counts.items(), key=lambda x: x[1]['total'], reverse=True):
            report += f"| {source} | {counts['total']} | {counts['high']} |\n"

        report += """
---

## All URLs Referenced

<details>
<summary>Click to expand ({} URLs)</summary>

""".format(len(self.urls))

        for url in sorted(self.urls):
            report += f"- {url}\n"
        
        report += "\n</details>\n"

        return report


def main():
    parser = argparse.ArgumentParser(description='Merge research findings')
    parser.add_argument('session_path', help='Path to research session')
    parser.add_argument('--output', '-o', help='Output file path', default=None)
    
    args = parser.parse_args()
    
    merger = FindingsMerger(args.session_path)
    report = merger.merge()
    
    if args.output:
        output_path = Path(args.output)
        output_path.write_text(report, encoding='utf-8')
        print(f"\nReport written to: {output_path}")
    else:
        # Write to session directory
        output_path = Path(args.session_path) / "03-synthesis" / "merged-findings.md"
        output_path.write_text(report, encoding='utf-8')
        print(f"\nReport written to: {output_path}")
    
    print("\nMerge complete!")


if __name__ == "__main__":
    main()
