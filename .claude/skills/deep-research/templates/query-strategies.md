# Query Generation Strategies

Use these strategies to generate comprehensive query variations for any research topic.

## Strategy Categories

### 1. Terminology Variations
Generate queries using different terms for the same concept:

```
Base: "RAG architecture"
Variations:
- "retrieval augmented generation architecture"
- "RAG system design"
- "RAG pipeline architecture"
- "vector search + LLM architecture"
- "semantic search augmented LLM"
```

### 2. Problem-Solution Framing
Frame the same topic as problem vs solution:

```
Solution frame:
- "RAG best practices"
- "RAG implementation guide"
- "how to build RAG"

Problem frame:
- "RAG not working"
- "RAG common issues"
- "RAG troubleshooting"
- "RAG performance problems"
```

### 3. Specificity Levels
Vary from broad to specific:

```
Broad:
- "RAG architecture"

Medium:
- "RAG architecture for enterprise"
- "production RAG system"

Specific:
- "RAG architecture langchain postgresql"
- "RAG chunk size optimization"
```

### 4. Site-Specific Searches
Target specific valuable sources:

```
GitHub:
- "site:github.com RAG production"
- "site:github.com/issues RAG performance"

Academic:
- "site:arxiv.org retrieval augmented generation"
- "site:semanticscholar.org RAG LLM"

Community:
- "site:reddit.com RAG architecture"
- "site:stackoverflow.com RAG implementation"
- "site:news.ycombinator.com RAG"
```

### 5. Time-Bounded Searches
Add temporal context:

```
Recent:
- "RAG architecture 2025"
- "RAG best practices 2024 2025"
- "latest RAG approaches"

Historical context:
- "RAG evolution since GPT"
```

### 6. Comparison Queries
Compare alternatives:

```
Direct comparison:
- "RAG vs fine-tuning"
- "RAG vs long context"
- "langchain vs llamaindex RAG"

Alternative seeking:
- "RAG alternatives"
- "instead of RAG"
```

### 7. Implementation Queries
Focus on practical implementation:

```
Code-focused:
- "RAG implementation python"
- "RAG code example"
- "RAG tutorial with code"

Stack-specific:
- "RAG langchain tutorial"
- "RAG openai embeddings"
- "RAG pinecone implementation"
```

### 8. Expert/Authority Queries
Seek authoritative sources:

```
- "RAG architecture anthropic"
- "RAG best practices openai"
- "RAG paper google research"
```

### 9. Negative/Warning Queries
Learn from failures:

```
- "RAG pitfalls"
- "RAG mistakes to avoid"
- "why RAG fails"
- "RAG anti-patterns"
```

### 10. Use Case Queries
Target specific applications:

```
- "RAG for customer support"
- "RAG for code documentation"
- "RAG for legal documents"
```

## Query Generation Template

For topic `{TOPIC}`, generate queries using this template:

```markdown
## Research Queries for: {TOPIC}

### Foundational Queries
1. "{TOPIC}" (base search)
2. "{TOPIC} explained"
3. "{TOPIC} overview"
4. "{TOPIC} introduction"

### Technical Deep-Dive
5. "{TOPIC} architecture"
6. "{TOPIC} implementation"
7. "{TOPIC} how it works"
8. "{TOPIC} under the hood"

### Best Practices & Patterns
9. "{TOPIC} best practices"
10. "{TOPIC} design patterns"
11. "{TOPIC} production ready"

### Problems & Solutions
12. "{TOPIC} issues"
13. "{TOPIC} troubleshooting"
14. "{TOPIC} common problems"
15. "why {TOPIC} not working"

### Comparisons
16. "{TOPIC} vs {ALTERNATIVE1}"
17. "{TOPIC} vs {ALTERNATIVE2}"
18. "{TOPIC} alternatives"
19. "best {TOPIC} approach"

### Source-Specific
20. "site:github.com {TOPIC}"
21. "site:arxiv.org {TOPIC}"
22. "site:reddit.com {TOPIC}"
23. "site:stackoverflow.com {TOPIC}"
24. "site:news.ycombinator.com {TOPIC}"

### Time-Bounded
25. "{TOPIC} 2025"
26. "{TOPIC} latest"
27. "{TOPIC} recent developments"

### Implementation-Focused
28. "{TOPIC} example code"
29. "{TOPIC} tutorial"
30. "{TOPIC} step by step"
```

## Domain-Specific Query Templates

### For Software Architecture Topics
```
- "{TOPIC} microservices"
- "{TOPIC} scalability"
- "{TOPIC} high availability"
- "{TOPIC} distributed systems"
```

### For Machine Learning Topics
```
- "{TOPIC} benchmark"
- "{TOPIC} evaluation metrics"
- "{TOPIC} paper"
- "{TOPIC} dataset"
- "{TOPIC} SOTA state of the art"
```

### For DevOps Topics
```
- "{TOPIC} kubernetes"
- "{TOPIC} docker"
- "{TOPIC} CI/CD"
- "{TOPIC} infrastructure as code"
```

### For Security Topics
```
- "{TOPIC} vulnerabilities"
- "{TOPIC} CVE"
- "{TOPIC} security best practices"
- "{TOPIC} penetration testing"
```

## Error Message Query Strategies

When researching error messages:

```
Exact match (most specific):
- "{exact error message}"

First line only:
- "{first line of error}"

Error code:
- "{error code}"

Without specifics:
- "{error type} {context}"

With library name:
- "{library} {error type}"
```

## Output: Generated Queries Log

Save generated queries to research session:

```markdown
# Generated Queries: {TOPIC}

Generated: {timestamp}

## Priority 1: Core Understanding
1. {query}
2. {query}

## Priority 2: Deep Technical
3. {query}
4. {query}

## Priority 3: Community Insights
5. {query}
6. {query}

## Priority 4: Validation & Verification
7. {query}
8. {query}

## Queries by Source
### GitHub-targeted
- {query}

### Academic-targeted
- {query}

### Community-targeted
- {query}
```
