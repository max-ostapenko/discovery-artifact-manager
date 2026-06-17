---
date: 2026-06-17
api: pagespeedonline.v5
service: PageSpeed Insights
title: "New 'Agentic Browsing' category added to Lighthouse audits"
impact: medium
breaking: false
tags: ["Lighthouse", "AI", "Web Performance", "SEO"]
interesting_score: 7
---

# New 'Agentic Browsing' category added to Lighthouse audits

**Date:** 2026-06-17  
**API:** `pagespeedonline.v5`  
**Impact:** Medium  

## Summary

PageSpeed Insights has introduced a new 'agentic-browsing' category to its Lighthouse reports, focusing on how AI agents interact with web content.

## Details

The Categories schema now includes an `agentic-browsing` property, which references the `LighthouseCategoryV5` schema. This addition indicates a shift toward measuring how well web pages accommodate autonomous agents or LLM-based browsers. Developers consuming PageSpeed reports via the API can now access this specific set of audits to evaluate their site's compatibility with the emerging 'agentic' web.

**Tags:** `Lighthouse` `AI` `Web Performance` `SEO`
