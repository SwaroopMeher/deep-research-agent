# Research Session Initialization Template

Use this template to initialize a new research session folder.

## Directory Structure

Create the following structure:

```
.claude/research-sessions/{YYYY-MM-DD}-{topic-slug}/
├── 00-research-plan.md          # Initial plan and query variations
├── 01-search-results/           # Raw search results by source
│   ├── coverage-matrix.md       # Track source coverage
│   └── {source}-{timestamp}.md  # Individual search results
├── 02-deep-dives/               # Detailed analysis of promising leads
│   └── {topic-slug}.md          # Deep-dive reports
├── 03-synthesis/                # Combined findings and patterns
│   └── current-understanding.md # Running synthesis document
├── 04-validation/               # Verification and cross-references
│   └── verification-log.md      # Validation results
└── FINAL-REPORT.md              # Comprehensive final report
```

## 00-research-plan.md Template

```markdown
# Research Plan: {Topic}

**Session ID**: {YYYY-MM-DD}-{topic-slug}
**Created**: {ISO timestamp}
**Status**: In Progress

---

## Research Question

{Clear, specific statement of what we're trying to learn}

**Scope**:
- In scope: {what's included}
- Out of scope: {what we're not investigating}

**Context**: 
{Why is this research needed? What will the results be used for?}

---

## Success Criteria

Research is complete when:
- [ ] Main question answered with {high/medium} confidence
- [ ] {N}+ independent sources consulted
- [ ] Key alternatives compared
- [ ] Practical implementation path identified
- [ ] Major risks/caveats documented

---

## Initial Hypotheses

Before research, our assumptions are:
1. {Hypothesis 1}
2. {Hypothesis 2}
3. {Hypothesis 3}

*These will be validated or refuted during research.*

---

## Key Terms & Concepts

| Term | Definition | Notes |
|------|------------|-------|
| {term} | {definition} | {any notes} |
| {term} | {definition} | {any notes} |

---

## Query Variations Generated

### Core Queries
1. "{query1}"
2. "{query2}"
3. "{query3}"

### Technical Deep-Dive Queries
4. "{query4}"
5. "{query5}"

### Community/Practical Queries
6. "{query6}"
7. "{query7}"

### Comparison Queries
8. "{query8}"
9. "{query9}"

### Source-Specific Queries
10. "site:github.com {query10}"

---

## Source Priority

For this research topic, prioritize:

1. **High Priority**: {source types most likely to have answers}
2. **Medium Priority**: {source types for additional perspective}
3. **Low Priority**: {source types for completeness}

---

## Known Starting Points

Resources we already know about:
- {URL or reference} - {what it covers}
- {URL or reference} - {what it covers}

---

## Time/Iteration Budget

- **Target iterations**: {N}
- **Queries per iteration**: {N}
- **Deep-dives per iteration**: {N}
- **Max total time**: {if applicable}

---

## Research Log

### {timestamp} - Session Start
- Initialized research session
- Generated {N} query variations
- Beginning iteration 1

### {timestamp} - Iteration 1 Complete
- Searched {N} sources
- Found {N} promising leads
- Key finding: {brief}
- Gaps identified: {brief}

*Continue logging each major step*
```

## 03-synthesis/current-understanding.md Initial Template

```markdown
# Current Understanding: {Topic}

**Last Updated**: {timestamp}
**Iteration**: 0 (not yet started)
**Confidence Level**: None yet

---

## Executive Summary

*To be filled after first research iteration.*

---

## Findings

### High Confidence
*None yet*

### Medium Confidence  
*None yet*

### Low Confidence
*None yet*

---

## Open Questions

- [ ] {The main research question}
- [ ] {Sub-question 1}
- [ ] {Sub-question 2}

---

## Contradictions & Debates
*None identified yet*

---

## Preliminary Recommendations
*None yet - research not started*

---

## Source Quality Summary
| Source | Type | Credibility | Key Contribution |
|--------|------|-------------|------------------|
| *None yet* | | | |
```

## 04-validation/verification-log.md Initial Template

```markdown
# Validation Log: {Topic}

**Created**: {timestamp}
**Status**: Pending research completion

---

## Validation Queue

*Findings to validate will be added here as research progresses.*

---

## Completed Validations

*None yet*

---

## Validation Summary

*To be completed after validation phase*
```

## FINAL-REPORT.md Placeholder

```markdown
# Deep Research Report: {Topic}

**Status**: Research in progress
**Generated**: Pending

---

*This report will be generated upon research completion.*

*Current progress can be found in:*
- `03-synthesis/current-understanding.md` - Latest synthesis
- `00-research-plan.md` - Research log

---
```

## Session Initialization Checklist

When starting a new research session:

- [ ] Create dated folder in `.claude/research-sessions/`
- [ ] Copy and fill out `00-research-plan.md`
- [ ] Copy `coverage-matrix.md` to `01-search-results/`
- [ ] Initialize `03-synthesis/current-understanding.md`
- [ ] Initialize `04-validation/verification-log.md`
- [ ] Create placeholder `FINAL-REPORT.md`
- [ ] Generate initial query variations
- [ ] Confirm research scope with user (if ambiguous)
- [ ] Begin iteration 1
