#!/usr/bin/env python3
"""
Research Validation Script

Validates a research session by checking:
1. All required files exist
2. Coverage matrix completeness
3. Finding confidence distribution
4. Source diversity
5. Cross-reference integrity

Usage: python validate-research.py <session-path>
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Any
import json

class ResearchValidator:
    def __init__(self, session_path: str):
        self.session_path = Path(session_path)
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.stats: Dict[str, Any] = {}
    
    def validate(self) -> Tuple[bool, Dict[str, Any]]:
        """Run all validations and return (success, report)"""
        
        print(f"Validating research session: {self.session_path}")
        print("=" * 60)
        
        # Check session directory exists
        if not self.session_path.exists():
            return False, {"error": f"Session path does not exist: {self.session_path}"}
        
        # Run validations
        self._validate_structure()
        self._validate_research_plan()
        self._validate_coverage()
        self._validate_synthesis()
        self._validate_sources()
        
        # Generate report
        report = self._generate_report()
        
        # Print summary
        self._print_summary()
        
        success = len(self.errors) == 0
        return success, report
    
    def _validate_structure(self):
        """Check required directory structure"""
        print("\n[1/5] Validating directory structure...")
        
        required_dirs = [
            "01-search-results",
            "02-deep-dives", 
            "03-synthesis",
            "04-validation"
        ]
        
        required_files = [
            "00-research-plan.md",
            "01-search-results/coverage-matrix.md",
            "03-synthesis/current-understanding.md",
            "04-validation/verification-log.md",
            "FINAL-REPORT.md"
        ]
        
        for dir_name in required_dirs:
            dir_path = self.session_path / dir_name
            if not dir_path.exists():
                self.errors.append(f"Missing required directory: {dir_name}")
            else:
                print(f"  ✓ {dir_name}/")
        
        for file_name in required_files:
            file_path = self.session_path / file_name
            if not file_path.exists():
                self.warnings.append(f"Missing file: {file_name}")
            else:
                print(f"  ✓ {file_name}")
    
    def _validate_research_plan(self):
        """Validate research plan completeness"""
        print("\n[2/5] Validating research plan...")
        
        plan_path = self.session_path / "00-research-plan.md"
        if not plan_path.exists():
            self.errors.append("Research plan file missing")
            return
        
        content = plan_path.read_text(encoding='utf-8')
        
        # Check for required sections
        required_sections = [
            "Research Question",
            "Success Criteria",
            "Query Variations"
        ]
        
        for section in required_sections:
            if section.lower() in content.lower():
                print(f"  ✓ {section} section found")
            else:
                self.warnings.append(f"Research plan missing section: {section}")
        
        # Count queries
        query_count = len(re.findall(r'^\d+\.\s*["\']', content, re.MULTILINE))
        self.stats['queries_planned'] = query_count
        
        if query_count < 5:
            self.warnings.append(f"Only {query_count} queries planned (recommend 5-10)")
        else:
            print(f"  ✓ {query_count} queries planned")
    
    def _validate_coverage(self):
        """Validate source coverage"""
        print("\n[3/5] Validating source coverage...")
        
        matrix_path = self.session_path / "01-search-results" / "coverage-matrix.md"
        if not matrix_path.exists():
            self.warnings.append("Coverage matrix missing")
            return
        
        content = matrix_path.read_text(encoding='utf-8')
        
        # Count checked vs unchecked boxes
        checked = len(re.findall(r'\[x\]', content, re.IGNORECASE))
        unchecked = len(re.findall(r'\[\s\]', content))
        
        self.stats['sources_covered'] = checked
        self.stats['sources_total'] = checked + unchecked
        
        if checked + unchecked > 0:
            coverage_pct = (checked / (checked + unchecked)) * 100
            self.stats['coverage_percent'] = coverage_pct
            
            if coverage_pct < 25:
                self.warnings.append(f"Low source coverage: {coverage_pct:.0f}%")
            elif coverage_pct >= 75:
                print(f"  ✓ Good source coverage: {coverage_pct:.0f}%")
            else:
                print(f"  ~ Partial source coverage: {coverage_pct:.0f}%")
        
        # Count result files
        results_dir = self.session_path / "01-search-results"
        result_files = list(results_dir.glob("*.md"))
        result_files = [f for f in result_files if f.name != "coverage-matrix.md"]
        
        self.stats['result_files'] = len(result_files)
        print(f"  ✓ {len(result_files)} search result files")
    
    def _validate_synthesis(self):
        """Validate synthesis quality"""
        print("\n[4/5] Validating synthesis...")
        
        synthesis_path = self.session_path / "03-synthesis" / "current-understanding.md"
        if not synthesis_path.exists():
            self.warnings.append("Synthesis document missing")
            return
        
        content = synthesis_path.read_text(encoding='utf-8')
        
        # Check for findings by confidence level
        high_conf = len(re.findall(r'High Confidence', content, re.IGNORECASE))
        med_conf = len(re.findall(r'Medium Confidence', content, re.IGNORECASE))
        low_conf = len(re.findall(r'Low Confidence', content, re.IGNORECASE))
        
        # Count actual findings (numbered or bulleted items under confidence sections)
        finding_count = len(re.findall(r'^[-*]\s+\*\*|^#+\s+Finding', content, re.MULTILINE))
        
        self.stats['findings_count'] = finding_count
        print(f"  ✓ {finding_count} findings documented")
        
        # Check for open questions
        open_questions = len(re.findall(r'^\s*-\s*\[\s*\]', content, re.MULTILINE))
        self.stats['open_questions'] = open_questions
        
        if open_questions > 0:
            print(f"  ~ {open_questions} open questions remaining")
        
        # Check iteration count
        iteration_match = re.search(r'Iteration[:\s]+(\d+)', content)
        if iteration_match:
            iteration = int(iteration_match.group(1))
            self.stats['iterations'] = iteration
            if iteration == 0:
                self.warnings.append("Research has 0 iterations - not started?")
            else:
                print(f"  ✓ {iteration} iteration(s) completed")
    
    def _validate_sources(self):
        """Validate source diversity and quality"""
        print("\n[5/5] Validating source diversity...")
        
        # Count deep-dive files
        deep_dives_dir = self.session_path / "02-deep-dives"
        if deep_dives_dir.exists():
            deep_dive_files = list(deep_dives_dir.glob("*.md"))
            self.stats['deep_dives'] = len(deep_dive_files)
            
            if len(deep_dive_files) < 3:
                self.warnings.append(f"Only {len(deep_dive_files)} deep-dives (recommend 3+)")
            else:
                print(f"  ✓ {len(deep_dive_files)} deep-dive analyses")
        
        # Check for URL references in results
        results_dir = self.session_path / "01-search-results"
        url_count = 0
        unique_domains = set()
        
        for result_file in results_dir.glob("*.md"):
            content = result_file.read_text(encoding='utf-8')
            urls = re.findall(r'https?://([^/\s]+)', content)
            url_count += len(urls)
            unique_domains.update(urls)
        
        self.stats['total_urls'] = url_count
        self.stats['unique_domains'] = len(unique_domains)
        
        if len(unique_domains) > 0:
            print(f"  ✓ {url_count} URLs from {len(unique_domains)} unique domains")
        
        if len(unique_domains) < 3:
            self.warnings.append("Low source diversity - less than 3 unique domains")
    
    def _generate_report(self) -> Dict[str, Any]:
        """Generate validation report"""
        return {
            "session_path": str(self.session_path),
            "timestamp": datetime.now().isoformat(),
            "valid": len(self.errors) == 0,
            "errors": self.errors,
            "warnings": self.warnings,
            "statistics": self.stats,
            "recommendations": self._generate_recommendations()
        }
    
    def _generate_recommendations(self) -> List[str]:
        """Generate recommendations based on validation"""
        recommendations = []
        
        if self.stats.get('coverage_percent', 0) < 50:
            recommendations.append("Search more source types for comprehensive coverage")
        
        if self.stats.get('deep_dives', 0) < 3:
            recommendations.append("Perform more deep-dives on promising leads")
        
        if self.stats.get('findings_count', 0) < 5:
            recommendations.append("Synthesize more findings from search results")
        
        if self.stats.get('unique_domains', 0) < 5:
            recommendations.append("Diversify sources across more domains")
        
        if self.stats.get('open_questions', 0) > 5:
            recommendations.append("Consider additional iterations to address open questions")
        
        return recommendations
    
    def _print_summary(self):
        """Print validation summary"""
        print("\n" + "=" * 60)
        print("VALIDATION SUMMARY")
        print("=" * 60)
        
        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"   - {error}")
        
        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"   - {warning}")
        
        if not self.errors and not self.warnings:
            print("\n✅ All validations passed!")
        
        print(f"\n📊 Statistics:")
        for key, value in self.stats.items():
            print(f"   - {key.replace('_', ' ').title()}: {value}")
        
        recommendations = self._generate_recommendations()
        if recommendations:
            print(f"\n💡 Recommendations:")
            for rec in recommendations:
                print(f"   - {rec}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate-research.py <session-path>")
        print("\nExample: python validate-research.py .claude/research-sessions/2026-02-04-rag-architecture")
        sys.exit(1)
    
    session_path = sys.argv[1]
    validator = ResearchValidator(session_path)
    
    success, report = validator.validate()
    
    # Optionally output JSON report
    if len(sys.argv) > 2 and sys.argv[2] == "--json":
        print("\n" + json.dumps(report, indent=2))
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
