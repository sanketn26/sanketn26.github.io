## Learning and building in public 👋

After years building software, platforms, and distributed systems inside
companies, I'm starting a different chapter: exploring ideas, building
open-source software, writing, and sharing what I learn along the way.

The material covers defensive security, applied machine learning, AI frameworks
such as LangChain, LangGraph, and CrewAI, production AI engineering, data
engineering, and senior/staff-level system design and interview preparation.

No paywalls or ads—just clear Markdown lessons, runnable exercises, and
interactive simulations, all available on GitHub Pages.

This repository is the hub site at <https://sanketn26.github.io/>. It has three
main threads:

- **Projects** (`docs/projects.md`) — open-source experiments and early prototypes.
- **Learning notes** (`docs/notes-2-courses.md`) — courses grown from working notes, each in its own repo.
- **Writing** (`docs/articles.md`) — a dated list of long-form articles
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

### Explore the Notes 2 Courses

| Course | What you'll learn |
| --- | --- |
| [Defensive Security Engineering](https://sanketn26.github.io/learn-security/) | Visual-first, hands-on cybersecurity for software engineers. |
| [Learn ML](https://sanketn26.github.io/learn-ml/) | Applied machine learning and practical AI frameworks. |
| [AI Engineering](https://sanketn26.github.io/AIEngineering/) | Build systems around modern models without treating the models as magic. |
| [Senior Engineer Academy](https://sanketn26.github.io/interview-prep/) | Prepare for system design, DSA, and behavioural interviews at senior, staff, and lead levels. |
| [Data Engineering Academy](https://sanketn26.github.io/data-engineering/) | Intuition-first, production-focused modern data systems. |
