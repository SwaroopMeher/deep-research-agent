# Deep Research Agent for Claude Code

An autonomous deep research orchestrator that performs comprehensive, multi-source research using parallel sub-agents and recursive planning. Inspired by Gemini Deep Research methodology.

![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Features

- **Parallel Breadth Searches**: Multiple sub-agents search across different sources simultaneously
- **Recursive Depth Exploration**: Follow promising leads through citation chains and references
- **Persistent Memory**: All findings saved to structured markdown files (not relying on context)
- **Iterative Refinement**: Research loop with clear halt conditions
- **Multi-Source Coverage**: 20+ source types across 5 tiers (GitHub, arXiv, Reddit, Stack Overflow, academic papers, international forums)
- **Query Variation**: Generates 5-10 query variations per topic for comprehensive coverage
- **Validation Phase**: Cross-references and verifies findings before conclusions

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│           DEEP RESEARCH ORCHESTRATOR (SKILL.md)             │
│     "The Brain" - Plans, coordinates, iterates, halts       │
├─────────────────────────────────────────────────────────────┤
│                    SUB-AGENTS (Parallel)                    │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐        │
│  │ web-research │ │   source-    │ │  research-   │        │
│  │    -scout    │ │  specialist  │ │  synthesizer │        │
│  │  (Breadth)   │ │   (Depth)    │ │  (Combine)   │        │
│  └──────────────┘ └──────────────┘ └──────────────┘        │
│  ┌──────────────┐                                          │
│  │  research-   │                                          │
│  │  validator   │                                          │
│  │  (Verify)    │                                          │
│  └──────────────┘                                          │
├─────────────────────────────────────────────────────────────┤
│          MEMORY SYSTEM (research-sessions/)                 │
│  00-research-plan.md → 01-search-results/ → 02-deep-dives/ │
│  → 03-synthesis/ → 04-validation/ → FINAL-REPORT.md        │
└─────────────────────────────────────────────────────────────┘
```

## Installation

### Quick Install (Recommended)

Clone this repo into your home directory and the agents/skills will be available globally:

```bash
# Clone the repository
git clone https://github.com/SwaroopMeher/deep-research-agent.git

# Copy to Claude Code's config directory
cp -r deep-research-agent/.claude/* ~/.claude/

# Make scripts executable
chmod +x ~/.claude/skills/deep-research/scripts/*.sh
```

### Project-Level Install

To install for a specific project only:

```bash
# Navigate to your project
cd /path/to/your/project

# Clone the repository
git clone https://github.com/SwaroopMeher/deep-research-agent.git temp-agent

# Copy to project's .claude directory
mkdir -p .claude
cp -r temp-agent/.claude/* .claude/

# Clean up
rm -rf temp-agent

# Make scripts executable
chmod +x .claude/skills/deep-research/scripts/*.sh
```

### Manual Install

1. Download the repository as a ZIP file
2. Extract the `.claude` folder
3. Copy contents to `~/.claude/` (global) or `.claude/` (project-level)

## Usage

### Basic Usage

In Claude Code, simply ask for deep research:

```
Research the best RAG architecture for my project
```

Or invoke the skill explicitly:

```
/deep-research What are the latest advancements in vector databases for production RAG systems?
```

### Example Queries

```
# Technical architecture research
/deep-research Compare different approaches for implementing real-time collaborative editing

# Library/framework comparison
/deep-research What's the best state management solution for React in 2025?

# Debugging assistance
/deep-research How to fix "CUDA out of memory" errors when fine-tuning LLMs

# Best practices research
/deep-research Production-ready patterns for microservices authentication

# Academic research
/deep-research Latest research on retrieval-augmented generation for knowledge-intensive tasks
```

### Research Depth Options

When starting research, you can specify:

- **Quick**: Fast overview, 1-2 iterations, top sources only
- **Standard**: Balanced depth, 3-4 iterations, comprehensive coverage
- **Exhaustive**: Maximum depth, 5+ iterations, all source tiers

```
/deep-research [exhaustive] What are all the ways to optimize LLM inference latency?
```

## Research Workflow

1. **Planning Phase**
   - Confirm research question and scope
   - Generate 5-10 query variations
   - Initialize research session directory

2. **Search Phase (Parallel)**
   - Launch multiple search sub-agents
   - Cover all relevant source types
   - Save raw results to `01-search-results/`

3. **Deep-Dive Phase**
   - Analyze promising leads in detail
   - Follow citation chains
   - Save analyses to `02-deep-dives/`

4. **Synthesis Phase**
   - Combine findings across sources
   - Identify patterns, consensus, and conflicts
   - Update `03-synthesis/current-understanding.md`

5. **Validation Phase**
   - Cross-reference key findings
   - Verify code examples and claims
   - Update `04-validation/verification-log.md`

6. **Iteration Decision**
   - Check halt conditions
   - Plan next iteration if needed

7. **Final Report**
   - Generate comprehensive `FINAL-REPORT.md`

## Source Coverage

### Tier 1: Primary Technical (Always Searched)
- GitHub Issues & Discussions
- Stack Overflow
- Official Documentation
- GitHub READMEs & Wikis

### Tier 2: Community Knowledge (High Value)
- Reddit (relevant subreddits)
- Hacker News
- Dev.to / Medium / Hashnode
- Discord/Slack archives

### Tier 3: Academic (For Depth)
- arXiv
- Google Scholar
- Semantic Scholar
- Hugging Face Papers

### Tier 4: International (Hidden Gems)
- CSDN (Chinese)
- V2EX (Chinese)
- Qiita (Japanese)
- Habr (Russian)

### Tier 5: Real-Time
- X/Twitter
- LinkedIn
- YouTube (transcripts)

## Halt Conditions

Research automatically stops when:

1. ✅ Main question answered with high confidence
2. 🔄 Saturation: Last 2 iterations produced no new findings
3. 🛑 Maximum 5 iterations reached
4. ✓✓✓ Findings confirmed by 3+ independent sources
5. 🖐️ User requests to stop

## Memory System

All research is persisted to files in the **project root** (outside `.claude`):

```
research-sessions/
└── 2025-02-04-rag-architecture/
    ├── 00-research-plan.md          # Plan, queries, research log
    ├── 01-search-results/
    │   ├── coverage-matrix.md       # Source tracking
    │   ├── github-search-001.md     # Search results
    │   └── arxiv-search-001.md
    ├── 02-deep-dives/
    │   ├── langchain-rag.md         # Deep analysis
    │   └── rag-paper-2024.md
    ├── 03-synthesis/
    │   ├── current-understanding.md # Running synthesis
    │   └── merged-findings.md       # Merged from searches
    ├── 04-validation/
    │   └── verification-log.md      # Validation results
    └── FINAL-REPORT.md              # Comprehensive report
```

## Helper Scripts

### Initialize a Research Session

```bash
~/.claude/skills/deep-research/scripts/init-research-session.sh "your topic"
```

### Validate Research Completeness

```bash
python ~/.claude/skills/deep-research/scripts/validate-research.py research-sessions/2025-02-04-your-topic/
```

### Merge Findings from Multiple Sources

```bash
python ~/.claude/skills/deep-research/scripts/merge-findings.py research-sessions/2025-02-04-your-topic/
```

### Generate Final Report

```bash
python ~/.claude/skills/deep-research/scripts/generate-final-report.py research-sessions/2025-02-04-your-topic/
```

## Components

### Main Skill

| File | Description |
|------|-------------|
| `.claude/skills/deep-research/SKILL.md` | The orchestrator "brain" with comprehensive instructions |

### Sub-Agents

| File | Description |
|------|-------------|
| `.claude/agents/web-research-scout.md` | Fast parallel web searches |
| `.claude/agents/source-specialist.md` | Deep-dive analysis for specific source types |
| `.claude/agents/research-synthesizer.md` | Combines findings, identifies patterns |
| `.claude/agents/research-validator.md` | Cross-references and verifies claims |

### Templates

| File | Description |
|------|-------------|
| `templates/query-strategies.md` | Query generation patterns (10+ strategies) |
| `templates/source-coverage.md` | Source tracking matrix |
| `templates/research-session-init.md` | Session initialization guide |

### Scripts

| File | Description |
|------|-------------|
| `scripts/init-research-session.sh` | Initialize session folders |
| `scripts/validate-research.py` | Validate research completeness |
| `scripts/merge-findings.py` | Merge findings from multiple sources |
| `scripts/generate-final-report.py` | Compile final report |

## Requirements

- **Claude Code** (CLI or VS Code extension)
- **Python 3.7+** (for helper scripts)
- **Bash** (for shell scripts)

No additional dependencies required - uses only built-in Python libraries.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Areas for Contribution

- Additional source-specific analysis templates
- New query generation strategies
- Improved synthesis algorithms
- Better validation heuristics
- Internationalization support

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

- Inspired by [Gemini Deep Research](https://gemini.google/overview/deep-research/)
- Built for [Claude Code](https://code.claude.com)
- Uses the [Agent Skills](https://agentskills.io) open standard

## Author

**Swaroop Meher** - [@SwaroopMeher](https://github.com/SwaroopMeher)

---

*If this agent helps your research, consider giving it a ⭐!*
