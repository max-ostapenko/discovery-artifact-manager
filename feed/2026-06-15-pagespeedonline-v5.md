---
date: 2026-06-15
api: pagespeedonline.v5
service: PageSpeed Insights
title: "New Agentic Browsing Category in PageSpeed Reports"
impact: low
breaking: false
tags: ["Lighthouse", "Performance", "AI", "PageSpeed"]
interesting_score: 5
---

# New Agentic Browsing Category in PageSpeed Reports

**Date:** 2026-06-15  
**API:** `pagespeedonline.v5`  
**Impact:** Low  

## Summary

The PageSpeed Insights API now includes an 'agentic-browsing' category in its Lighthouse reports, signaling a shift toward auditing for AI-driven web navigation.

## Details

A new property `agentic-browsing` has been added to the `Categories` schema, referencing the `LighthouseCategoryV5` type. This category is designed to contain audits related to how AI agents or automated browsers interact with and perceive a page, allowing developers to programmatically retrieve metrics specifically for agentic web use cases.

**Tags:** `Lighthouse` `Performance` `AI` `PageSpeed`
