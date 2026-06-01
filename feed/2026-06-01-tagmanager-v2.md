---
date: 2026-06-01
api: tagmanager.v2
service: Google Tag Manager
title: "New automatic number conversion for GTM variables"
impact: low
breaking: false
tags: ["tag-manager", "variables", "data-formatting"]
interesting_score: 4
---

# New automatic number conversion for GTM variables

**Date:** 2026-06-01  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager variables now support automatic decimal separator detection when converting values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' option for the convertToNumber property. This allows the API to handle various decimal formats automatically during type conversion, which is particularly useful for internationalized data where decimal separators (dots vs. commas) vary by locale.

**Tags:** `tag-manager` `variables` `data-formatting`
