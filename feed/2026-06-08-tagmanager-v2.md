---
date: 2026-06-08
api: tagmanager.v2
service: Tag Manager
title: "New Automatic Decimal Detection for Variable Formatting"
impact: low
breaking: false
tags: ["tag-manager", "variables", "formatting"]
interesting_score: 4
---

# New Automatic Decimal Detection for Variable Formatting

**Date:** 2026-06-08  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager now supports automatic decimal separator detection when converting variable values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' option within the convertToNumber enum. This addition allows the API to handle numeric conversions more intelligently by automatically detecting the decimal separator, which simplifies data processing for internationalized sites where separators (dots vs. commas) vary by locale.

**Tags:** `tag-manager` `variables` `formatting`
