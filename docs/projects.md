---
title: Open-source experiments
description: Early open-source experiments in distributed caching, observability, agent context, and physics simulations.
hide:
  - toc
---

# What I’m working on

I’m using this phase to explore problems that have interested me for a long time.
Most of these projects are early. Some may work, some may change direction, and
some may simply teach me something useful. Everything here is open source on
[GitHub](https://github.com/sanketn26).

## Distributed systems

<div class="project-grid">

<article class="project-card">
  <span class="project-status status-prototype">Early prototype</span>
  <a href="https://github.com/sanketn26/gossipcache"><strong>GossipCache</strong></a>
  <span>In-process L1 cache with a memory-first L2 hub — hot reads stay local while the hub owns versions and invalidations.</span>
  <a class="project-related" href="https://sanketn26.github.io/interview-prep/system-design-exercises/distributed-cache/">Related lesson: Design: Distributed Cache</a>
  <b class="project-tags">Caching · Distributed systems</b>
</article>

<article class="project-card">
  <span class="project-status status-exploring">Exploring</span>
  <a href="https://github.com/sanketn26/luminate"><strong>Luminate</strong></a>
  <span>A high-cardinality observability system, built from the ground up for label dimensions that break traditional time-series databases.</span>
  <a class="project-related" href="https://sanketn26.github.io/data-engineering/architectures/observability/">Related lesson: Observability Platform Architecture</a>
  <b class="project-tags">Observability · Time series</b>
</article>

</div>

## AI and agents

<div class="project-grid">

<article class="project-card">
  <span class="project-status status-exploring">Exploring</span>
  <a href="https://github.com/sanketn26/cogneetree"><strong>Cogneetree</strong></a>
  <span>Hierarchical context for AI applications — persistent memory across Session → Activity → Task, so agents can reach past decisions and learnings.</span>
  <a class="project-related" href="https://sanketn26.github.io/AIEngineering/core/19-orchestration-patterns/">Related lesson: Orchestration patterns — memory</a>
  <b class="project-tags">Agents · Context management</b>
</article>

</div>

## Tools and learning

<div class="project-grid">

<article class="project-card">
  <span class="project-status status-exploring">Exploring</span>
  <a href="https://github.com/sanketn26/illusion"><strong>Illusion</strong></a>
  <span>Code-first physics simulations that reveal exactly where intuition breaks.</span>
  <b class="project-tags">Simulation · Learning</b>
</article>

</div>
