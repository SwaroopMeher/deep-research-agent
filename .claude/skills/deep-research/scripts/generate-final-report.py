#!/usr/bin/env python3
"""
Generate Final Research Report

Compiles all research materials into a comprehensive final report.
Combines:
- Research plan and methodology
- Merged findings
- Synthesis
- Validation results

Usage: python generate-final-report.py <session-path>
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
import argparse


class ReportGenerator:
    def __init__(self, session_path: str):
        self.session_path = Path(session_path)
        self.topic = self._extract_topic()
        self.stats = {}
    
    def _extract_topic(self) -> str:
        """Extract topic from session folder name"""
        name = self.session_path.name
        # Remove date prefix
        parts = name.split('-', 3)
        if len(parts) >= 4:
            return parts[3].replace('-', ' ').title()
        return name
    
    def generate(self) -> str:
        """Generate the final research report"""
        
        print(f"Generating final report for: {self.topic}")
        
        # Collect all pieces
        research_plan = self._read_file("00-research-plan.md")
        synthesis = self._read_file("03-synthesis/current-understanding.md")
        validation = self._read_file("04-validation/verification-log.md")
        merged = self._read_file("03-synthesis/merged-findings.md")
        
        # Calculate statistics
        self._calculate_stats()
        
        # Build report
        return self._build_report(research_plan, synthesis, validation, merged)
    
    def _read_file(self, relative_path: str) -> Optional[str]:
        """Read a file if it exists"""
        file_path = self.session_path / relative_path
        if file_path.exists():
            return file_path.read_text(encoding='utf-8')
        return None
    
    def _calculate_stats(self):
        """Calculate research statistics"""
        
        # Count files in each directory
        results_dir = self.session_path / "01-search-results"
        deep_dives_dir = self.session_path / "02-deep-dives"
        
        self.stats['search_results'] = len(list(results_dir.glob("*.md"))) - 1 if results_dir.exists() else 0
        self.stats['deep_dives'] = len(list(deep_dives_dir.glob("*.md"))) if deep_dives_dir.exists() else 0
        
        # Extract iteration from synthesis
        synthesis = self._read_file("03-synthesis/current-understanding.md")
        if synthesis:
            match = re.search(r'Iteration[:\s]+(\d+)', synthesis)
            self.stats['iterations'] = int(match.group(1)) if match else 0
            
            # Count findings
            self.stats['findings'] = len(re.findall(r'^#+\s+Finding', synthesis, re.MULTILINE))
            
            # Extract confidence level
            conf_match = re.search(r'Confidence Level[:\s]+(\w+)', synthesis)
            self.stats['confidence'] = conf_match.group(1) if conf_match else 'Unknown'
    
    def _extract_section(self, content: str, section_name: str) -> str:
        """Extract a section from markdown content"""
        pattern = rf'^## {section_name}\s*\n(.*?)(?=^## |\Z)'
        match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        return match.group(1).strip() if match else ""
    
    def _build_report(self, plan: str, synthesis: str, validation: str, merged: str) -> str:
        """Build the final report"""
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        session_name = self.session_path.name
        
        # Extract key sections from synthesis if available
        exec_summary = ""
        high_confidence = ""
        recommendations = ""
        open_questions = ""
        
        if synthesis:
            exec_summary = self._extract_section(synthesis, "Executive Summary")
            high_confidence = self._extract_section(synthesis, "High Confidence Findings") or \
                             self._extract_section(synthesis, "Detailed Findings")
            recommendations = self._extract_section(synthesis, "Preliminary Recommendations") or \
                             self._extract_section(synthesis, "Recommendations")
            open_questions = self._extract_section(synthesis, "Open Questions") or \
                            self._extract_section(synthesis, "Remaining Knowledge Gaps")
        
        # Extract validation summary
        validation_summary = ""
        if validation:
            validation_summary = self._extract_section(validation, "Validation Summary") or \
                                self._extract_section(validation, "Completed Validations")
        
        report = f"""# Deep Research Report: {self.topic}

**Generated**: {timestamp}
**Session ID**: {session_name}
**Research Duration**: {self.stats.get('iterations', 'N/A')} iterations
**Overall Confidence**: {self.stats.get('confidence', 'N/A')}

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Methodology](#methodology)
3. [Key Findings](#key-findings)
4. [Recommendations](#recommendations)
5. [Validation Results](#validation-results)
6. [Limitations & Caveats](#limitations--caveats)
7. [Further Research](#further-research)
8. [Appendix](#appendix)

---

## Executive Summary

{exec_summary or "*No executive summary available - synthesis may be incomplete.*"}

### Quick Statistics

| Metric | Value |
|--------|-------|
| Research Iterations | {self.stats.get('iterations', 'N/A')} |
| Sources Searched | {self.stats.get('search_results', 'N/A')} |
| Deep-Dive Analyses | {self.stats.get('deep_dives', 'N/A')} |
| Findings Documented | {self.stats.get('findings', 'N/A')} |
| Confidence Level | {self.stats.get('confidence', 'N/A')} |

---

## Methodology

This research was conducted using the Deep Research methodology, which includes:

### Research Approach

1. **Query Generation**: Multiple query variations generated to maximize coverage
2. **Multi-Source Search**: Systematic search across technical documentation, community forums, academic papers, and real-time sources
3. **Deep-Dive Analysis**: Detailed analysis of the most promising sources
4. **Iterative Synthesis**: Progressive building of understanding across multiple iterations
5. **Validation**: Cross-referencing and verification of key findings

### Sources Covered

The research covered the following source categories:

- **Tier 1 (Primary Technical)**: GitHub Issues/Discussions, Stack Overflow, Official Documentation
- **Tier 2 (Community)**: Reddit, Hacker News, Dev.to, Medium
- **Tier 3 (Academic)**: arXiv, Google Scholar, Semantic Scholar
- **Tier 4 (International)**: CSDN, V2EX, Qiita (as available)
- **Tier 5 (Real-Time)**: Twitter/X, LinkedIn

### Research Questions

"""
        # Try to extract research questions from plan
        if plan:
            questions_match = re.search(r'## Research Question\s*\n(.*?)(?=^## |\Z)', plan, re.MULTILINE | re.DOTALL)
            if questions_match:
                report += questions_match.group(1).strip() + "\n\n"
            else:
                report += f"*Primary question*: What is the best approach for {self.topic}?\n\n"
        
        report += f"""---

## Key Findings

{high_confidence or "*Findings not yet synthesized. See 03-synthesis/current-understanding.md for latest progress.*"}

---

## Recommendations

{recommendations or "*Recommendations not yet formulated. Research may still be in progress.*"}

---

## Validation Results

{validation_summary or "*Validation not yet completed.*"}

### Confidence Assessment

Based on the research conducted:

- **Strongly Supported**: Findings confirmed by 3+ independent, credible sources
- **Moderately Supported**: Findings from 2 sources or strong expert opinion
- **Preliminary**: Single source or speculative findings that need verification

---

## Limitations & Caveats

### Methodology Limitations

1. **Search Bias**: Results may be biased toward sources that are well-indexed by search engines
2. **Temporal Limitations**: Research reflects information available at the time of the search
3. **Language Bias**: Primary focus on English-language sources
4. **Depth vs Breadth Trade-off**: Some topics may have been explored more thoroughly than others

### Findings Limitations

{open_questions or "*No specific limitations identified yet.*"}

---

## Further Research

### Remaining Questions

{open_questions or "*All primary questions addressed.*"}

### Suggested Next Steps

1. Validate key findings through practical experimentation
2. Monitor for new developments in rapidly evolving areas
3. Seek expert review of recommendations before implementation
4. Consider follow-up deep-dives on specific subtopics

---

## Appendix

### A. Session Files

The complete research session is stored at: `{self.session_path}`

**Directory Structure**:
```
{session_name}/
├── 00-research-plan.md          # Initial plan and methodology
├── 01-search-results/           # Raw search results ({self.stats.get('search_results', 0)} files)
├── 02-deep-dives/               # Deep-dive analyses ({self.stats.get('deep_dives', 0)} files)
├── 03-synthesis/                # Synthesis documents
├── 04-validation/               # Validation logs
└── FINAL-REPORT.md              # This report
```

### B. Research Timeline

See `00-research-plan.md` for detailed research log with timestamps.

### C. Full Source List

"""
        # Add merged findings summary if available
        if merged:
            urls_section = re.search(r'## All URLs Referenced(.*?)(?=^## |\Z)', merged, re.MULTILINE | re.DOTALL)
            if urls_section:
                report += urls_section.group(0)
            else:
                report += "See `03-synthesis/merged-findings.md` for complete source list.\n"
        else:
            report += "See individual files in `01-search-results/` for sources.\n"
        
        report += """
---

*This report was generated by the Deep Research system. For questions about methodology or findings, consult the detailed session files.*
"""
        
        return report


def main():
    parser = argparse.ArgumentParser(description='Generate final research report')
    parser.add_argument('session_path', help='Path to research session')
    parser.add_argument('--output', '-o', help='Output file path (default: FINAL-REPORT.md in session)', default=None)
    
    args = parser.parse_args()
    
    generator = ReportGenerator(args.session_path)
    report = generator.generate()
    
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = Path(args.session_path) / "FINAL-REPORT.md"
    
    output_path.write_text(report, encoding='utf-8')
    print(f"\nFinal report written to: {output_path}")
    print("\nReport generation complete!")


if __name__ == "__main__":
    main()
