---
title: Open-source projects
description: Open-source systems and tooling by Sanket Naik — distributed caching, durable execution, high-cardinality observability, agent context management, task processing, and trying my hand at Theoritical Physics
hide:
  - toc
---

# Projects

Systems/Projects I am building or in process of building currently. Everything here is open source on
[GitHub](https://github.com/sanketn26).

Each project carries its current stage: **Ideation** (design and notes),
**WIP** (actively being built), **Alpha** (runnable, rough edges), and
**Beta** (usable, stabilising). Most of these are early — the thinking is
further along than the code.

## Distributed systems

<div class="project-grid">

<a class="project-card" href="https://github.com/sanketn26/gossipcache" aria-label="GossipCache on GitHub">
  <span class="project-status status-ideation">Ideation</span>
  <strong>GossipCache</strong>
  <span>In-process L1 cache with a memory-first L2 hub — hot reads stay local while the hub owns versions and invalidations.</span>
  <b class="project-tags">Caching · Distributed systems</b>
</a>

<a class="project-card" href="https://github.com/sanketn26/niyanta" aria-label="Niyanta on GitHub">
  <span class="project-status status-ideation">Ideation</span>
  <strong>Niyanta</strong>
  <span>A durable activity execution engine: replay-based resume, managed retries, exactly-once child dispatch, and generation-fenced redistribution.</span>
  <b class="project-tags">Durable execution · Workflows</b>
</a>

<a class="project-card" href="https://github.com/sanketn26/luminate" aria-label="Luminate on GitHub">
  <span class="project-status status-ideation">Ideation</span>
  <strong>Luminate</strong>
  <span>A high-cardinality observability system, built from the ground up for label dimensions that break traditional time-series databases.</span>
  <b class="project-tags">Observability · Time series</b>
</a>

<a class="project-card" href="https://github.com/sanketn26/taskflow" aria-label="Taskwire on GitHub">
  <span class="project-status status-ideation">Ideation</span>
  <strong>Taskwire</strong>
  <span>A lightweight, opinionated, optionally distributed task processing framework for Python.</span>
  <b class="project-tags">Python · Task queues</b>
</a>

</div>

## AI and agents

<div class="project-grid">

<a class="project-card" href="https://github.com/sanketn26/cogneetree" aria-label="Cogneetree on GitHub">
  <span class="project-status status-ideation">Ideation</span>
  <strong>Cogneetree</strong>
  <span>Hierarchical context for AI applications — persistent memory across Session → Activity → Task, so agents can reach past decisions and learnings.</span>
  <b class="project-tags">Agents · Context management</b>
</a>

</div>

## Tools and learning

<div class="project-grid">

<a class="project-card" href="https://github.com/sanketn26/illusion" aria-label="Illusion on GitHub">
  <span class="project-status status-ideation">Ideation</span>
  <strong>Illusion</strong>
  <span>Code-first physics simulations that reveal exactly where intuition breaks.</span>
  <b class="project-tags">Simulation · Learning</b>
</a>

</div>
