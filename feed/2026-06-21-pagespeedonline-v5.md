---
date: 2026-06-21
api: pagespeedonline.v5
service: PageSpeed Insights
title: "New Agentic Browsing Category in PageSpeed Reports"
impact: low
breaking: false
tags: ["Lighthouse", "Web Performance", "AI Agents"]
interesting_score: 5
---

# New Agentic Browsing Category in PageSpeed Reports

**Date:** 2026-06-21  
**API:** `pagespeedonline.v5`  
**Impact:** Low  

## Summary

The PageSpeed Insights API now includes a new 'agentic-browsing' category in Lighthouse reports, designed to group audits related to AI-driven or automated browsing behaviors.

## Details

A new property `agentic-browsing` has been added to the `Categories` schema. This field references `LighthouseCategoryV5` and is intended to house audits specifically targeting 'agentic browsing' scenarios. This likely points toward how websites interact with LLM-based agents and automated crawlers that go beyond traditional SEO bots.

**Tags:** `Lighthouse` `Web Performance` `AI Agents`
