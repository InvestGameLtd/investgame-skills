# Security Policy

## Reporting a vulnerability

Email **app@investgame.net**. Please do not open a public issue for a security report.

This repository is generated: the skills are built from InvestGame's private source and
published here. Issues and pull requests are not monitored. For anything other than a
security report, contact app@investgame.net.

## Scope

The published content is skill documentation (Markdown), brand templates and assets, and three
code files under `skills/investgame-format/brand-kit/`: a PDF-rendering script
(`scripts/render_pdf.py`) that Claude may run on your machine when you ask for a PDF, and two
colour and chart helper modules (`assets/ig_helpers.py`, `assets/ig_helpers.js`). Nothing runs at
install time. It contains no credentials. Secret scanning and push protection are enabled on this repository.
