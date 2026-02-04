# Source Coverage Tracking

Track which sources have been searched for comprehensive research coverage.

## Source Coverage Matrix Template

Copy this to your research session at `01-search-results/coverage-matrix.md`:

```markdown
# Source Coverage Matrix

**Research Topic**: {topic}
**Last Updated**: {timestamp}

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
| ACL Anthology | [ ] | | | |

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

- **Total Sources Searched**: {N} / 20
- **Total Queries Executed**: {N}
- **Total Deep-Dives**: {N}
- **Coverage Gaps**: {list}

## Iteration History

### Iteration 1
- Sources: {list}
- Focus: {initial broad search}

### Iteration 2
- Sources: {list}
- Focus: {targeted gap-filling}

### Iteration N
...
```

## Source-Specific Search Strategies

### GitHub
```
Search URLs:
- Issues: github.com/search?type=issues&q={query}
- Discussions: github.com/search?type=discussions&q={query}
- Code: github.com/search?type=code&q={query}
- Repos: github.com/search?type=repositories&q={query}

Key strategies:
- Search in specific repos known to be relevant
- Filter by stars for quality
- Check "good first issue" for learning resources
- Look at closed issues for solutions
```

### Stack Overflow
```
Search tips:
- Use [tag] syntax: [python] [rag]
- Use quotes for exact phrases
- Sort by votes for community-validated answers
- Check "Linked" and "Related" questions

Quality signals:
- Accepted answer
- High vote count
- Recent activity
- Multiple answers to compare
```

### Reddit
```
Key subreddits by domain:
- AI/ML: r/MachineLearning, r/LocalLLaMA, r/artificial
- Programming: r/programming, r/learnprogramming, r/coding
- Specific: r/Python, r/rust, r/golang
- DevOps: r/devops, r/kubernetes, r/docker
- Career: r/cscareerquestions

Search tips:
- site:reddit.com/r/{subreddit} {query}
- Sort by "top" for quality, "new" for recent
- Check comment sections - gold is often in comments
```

### Hacker News
```
Search options:
- hn.algolia.com for full-text search
- site:news.ycombinator.com {query}

Quality signals:
- High point count
- Many comments
- Comments from known experts
- Links to original sources
```

### arXiv
```
Search URL: arxiv.org/search/?query={query}

Strategies:
- Search by subject area (cs.CL, cs.LG, cs.AI)
- Check "recent submissions" for latest
- Follow citation chains
- Look for survey papers for overviews

Quality signals:
- Citations (via Semantic Scholar)
- Author reputation
- Acceptance at major venues (noted in abstract)
```

### Official Documentation
```
Strategy:
- Find official docs first
- Check version-specific docs
- Look for "Guides" and "Tutorials" sections
- Check changelogs for recent updates
- Look for migration guides
```

### Dev.to / Medium
```
Quality signals:
- Author profile (follower count, other articles)
- Engagement (likes, comments)
- Recency
- Code examples included
- References to other sources

Caution:
- Variable quality
- May be outdated
- Sometimes promotional
```

## Coverage Quality Metrics

### Minimal Coverage (Quick Research)
- At least 3 different source types
- At least 5 total queries
- At least 2 deep-dives

### Standard Coverage
- At least 5 different source types
- All Tier 1 sources covered
- At least 10 total queries
- At least 5 deep-dives
- At least 1 academic source

### Comprehensive Coverage (Deep Research)
- All Tier 1-3 sources covered
- Selected Tier 4-5 sources
- 20+ queries executed
- 10+ deep-dives
- Cross-referenced findings
- Multiple iterations

### Exhaustive Coverage
- All sources in matrix
- Multiple queries per source
- 30+ total queries
- 15+ deep-dives
- All major leads followed
- Full validation cycle

## Gap Identification

After each iteration, check:

```markdown
## Gap Analysis

### Uncovered Source Types
- [ ] {source type not yet searched}

### Unanswered Questions
- [ ] {question from synthesis with no good answer}

### Low-Confidence Areas
- [ ] {finding with only single source}

### Missing Perspectives
- [ ] {viewpoint not represented - academic, practitioner, etc.}

### Temporal Gaps
- [ ] {old information that might have updates}
```

## Next Iteration Planning

Based on gaps, plan next iteration:

```markdown
## Next Iteration Plan

### Priority Sources to Search
1. {source} - reason: {gap it fills}
2. {source} - reason: {gap it fills}

### Targeted Queries
1. "{query}" - targets: {gap}
2. "{query}" - targets: {gap}

### Deep-Dive Candidates
1. {URL} - reason: {why promising}
2. {URL} - reason: {why promising}
```
