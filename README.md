## Learning in public 👋

Throughout my career, I've kept detailed notes on what I've learned through
hands-on experience. With the help of AI, I've organised and expanded those notes into
structured learning material that I can share with others.

The material covers defensive security, applied machine learning, AI frameworks
such as LangChain, LangGraph, and CrewAI, production AI engineering, data
engineering, and senior/staff-level system design and interview preparation.

No paywalls or ads—just clear Markdown lessons, runnable exercises, and
interactive simulations, all available on GitHub Pages.

This repository is the hub site at <https://sanketn26.github.io/>. It has four
sections:

- **Home** — landing page linking to everything below.
- **Note Courses** (`docs/note-courses.md`) — five courses grown from working notes, each its own repo.
- **Projects** (`docs/projects.md`) — open-source systems and tooling.
- **Articles** (`docs/articles.md`) — a dated list of long-form articles
  published on Medium.

### Adding an article

Add a `link-item` block to `docs/articles.md`, newest first:

```html
<a class="link-item" href="https://medium.com/...">
  <span class="link-date">2026-09-06</span>
  <strong>Article title</strong>
  <span>One-line summary.
  <span class="link-meta">Publication</span></span>
</a>
```

### Local preview

```bash
pip install -r requirements.txt
mkdocs serve
```

### Explore the note courses

| Note course | What you'll learn |
| --- | --- |
| [Defensive Security Engineering](https://sanketn26.github.io/learn-security/) | Visual-first, hands-on cybersecurity for software engineers. |
| [Learn ML](https://sanketn26.github.io/learn-ml/) | Applied machine learning and practical AI frameworks. |
| [AI Engineering](https://sanketn26.github.io/AIEngineering/) | Build from your first prompt through to production-ready agents. |
| [Senior Engineer Academy](https://sanketn26.github.io/interview-prep/) | Prepare for system design, DSA, and behavioural interviews at senior, staff, and lead levels. |
| [Data Engineering Academy](https://sanketn26.github.io/data-engineering/) | Intuition-first, production-focused modern data systems. |
