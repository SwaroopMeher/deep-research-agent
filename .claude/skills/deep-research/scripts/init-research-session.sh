#!/bin/bash
# Initialize a new deep research session
# Usage: ./init-research-session.sh "topic name"

set -e

# Get topic from argument or prompt
TOPIC="${1:-}"
if [ -z "$TOPIC" ]; then
    echo "Usage: $0 \"topic name\""
    exit 1
fi

# Create slug from topic
SLUG=$(echo "$TOPIC" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-//' | sed 's/-$//')

# Get today's date
DATE=$(date +%Y-%m-%d)

# Session directory (in project root, outside .claude)
SESSION_DIR="research-sessions/${DATE}-${SLUG}"

# Check if already exists
if [ -d "$SESSION_DIR" ]; then
    echo "Session directory already exists: $SESSION_DIR"
    echo "Either use existing session or choose a different topic name."
    exit 1
fi

echo "Creating research session: $SESSION_DIR"

# Create directory structure
mkdir -p "$SESSION_DIR/01-search-results"
mkdir -p "$SESSION_DIR/02-deep-dives"
mkdir -p "$SESSION_DIR/03-synthesis"
mkdir -p "$SESSION_DIR/04-validation"

# Create timestamp
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)

# Create 00-research-plan.md
cat > "$SESSION_DIR/00-research-plan.md" << EOF
# Research Plan: $TOPIC

**Session ID**: ${DATE}-${SLUG}
**Created**: $TIMESTAMP
**Status**: In Progress

---

## Research Question

{Clear, specific statement of what we're trying to learn about $TOPIC}

**Scope**:
- In scope: {what's included}
- Out of scope: {what we're not investigating}

**Context**: 
{Why is this research needed? What will the results be used for?}

---

## Success Criteria

Research is complete when:
- [ ] Main question answered with high/medium confidence
- [ ] 5+ independent sources consulted
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
| | | |

---

## Query Variations Generated

### Core Queries
1. "$TOPIC"
2. "$TOPIC explained"
3. "$TOPIC architecture"

### Technical Deep-Dive Queries
4. "$TOPIC implementation"
5. "$TOPIC best practices"

### Community/Practical Queries
6. "$TOPIC tutorial"
7. "site:reddit.com $TOPIC"

### Comparison Queries
8. "$TOPIC vs"
9. "$TOPIC alternatives"

### Source-Specific Queries
10. "site:github.com $TOPIC"

---

## Source Priority

For this research topic, prioritize:

1. **High Priority**: 
2. **Medium Priority**: 
3. **Low Priority**: 

---

## Known Starting Points

Resources we already know about:
- 

---

## Time/Iteration Budget

- **Target iterations**: 3-5
- **Queries per iteration**: 10-15
- **Deep-dives per iteration**: 3-5
- **Max total time**: No limit

---

## Research Log

### $TIMESTAMP - Session Start
- Initialized research session
- Ready for query generation
- Beginning iteration 1
EOF

# Create coverage matrix
cat > "$SESSION_DIR/01-search-results/coverage-matrix.md" << EOF
# Source Coverage Matrix

**Research Topic**: $TOPIC
**Last Updated**: $TIMESTAMP

## Coverage Status

### Tier 1: Primary Technical Sources
| Source | Queries Run | Results Found | Deep-Dives | Notes |
|--------|-------------|---------------|------------|-------|
| GitHub Issues | [ ] | | | |
| GitHub Discussions | [ ] | | | |
| Stack Overflow | [ ] | | | |
| Official Docs | [ ] | | | |
| GitHub READMEs | [ ] | | | |

### Tier 2: Community Knowledge
| Source | Queries Run | Results Found | Deep-Dives | Notes |
|--------|-------------|---------------|------------|-------|
| Reddit | [ ] | | | |
| Hacker News | [ ] | | | |
| Dev.to | [ ] | | | |
| Medium | [ ] | | | |
| Discord (archives) | [ ] | | | |

### Tier 3: Academic
| Source | Queries Run | Results Found | Deep-Dives | Notes |
|--------|-------------|---------------|------------|-------|
| arXiv | [ ] | | | |
| Google Scholar | [ ] | | | |
| Semantic Scholar | [ ] | | | |
| Hugging Face Papers | [ ] | | | |

### Tier 4: International
| Source | Queries Run | Results Found | Deep-Dives | Notes |
|--------|-------------|---------------|------------|-------|
| CSDN | [ ] | | | |
| V2EX | [ ] | | | |
| Qiita | [ ] | | | |
| Habr | [ ] | | | |

### Tier 5: Real-Time
| Source | Queries Run | Results Found | Deep-Dives | Notes |
|--------|-------------|---------------|------------|-------|
| X/Twitter | [ ] | | | |
| LinkedIn | [ ] | | | |
| YouTube | [ ] | | | |

## Coverage Summary

- **Total Sources Searched**: 0 / 20
- **Total Queries Executed**: 0
- **Total Deep-Dives**: 0
- **Coverage Gaps**: All sources

## Iteration History

*To be filled as research progresses*
EOF

# Create current understanding
cat > "$SESSION_DIR/03-synthesis/current-understanding.md" << EOF
# Current Understanding: $TOPIC

**Last Updated**: $TIMESTAMP
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

- [ ] {The main research question about $TOPIC}
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
EOF

# Create validation log
cat > "$SESSION_DIR/04-validation/verification-log.md" << EOF
# Validation Log: $TOPIC

**Created**: $TIMESTAMP
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
EOF

# Create final report placeholder
cat > "$SESSION_DIR/FINAL-REPORT.md" << EOF
# Deep Research Report: $TOPIC

**Status**: Research in progress
**Generated**: Pending
**Session**: ${DATE}-${SLUG}

---

*This report will be generated upon research completion.*

*Current progress can be found in:*
- \`03-synthesis/current-understanding.md\` - Latest synthesis
- \`00-research-plan.md\` - Research log

---
EOF

echo ""
echo "Research session initialized successfully!"
echo ""
echo "Session directory: $SESSION_DIR"
echo ""
echo "Created files:"
echo "  - 00-research-plan.md (fill in research question and scope)"
echo "  - 01-search-results/coverage-matrix.md"
echo "  - 03-synthesis/current-understanding.md"
echo "  - 04-validation/verification-log.md"
echo "  - FINAL-REPORT.md (placeholder)"
echo ""
echo "Next steps:"
echo "  1. Fill in the research question in 00-research-plan.md"
echo "  2. Generate query variations"
echo "  3. Begin research iteration 1"
