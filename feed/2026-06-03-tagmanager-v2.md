---
date: 2026-06-03
api: tagmanager.v2
service: Google Tag Manager
title: "New Automatic Number Conversion for GTM Variables"
impact: low
breaking: false
tags: ["tag-manager", "variables", "data-types"]
interesting_score: 4
---

# New Automatic Number Conversion for GTM Variables

**Date:** 2026-06-03  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager API now supports automatic decimal separator detection when converting variable values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' enum value for the convertToNumber property. This allows developers to programmatically configure variables to handle numeric conversion without manually specifying decimal formats, which is particularly useful for handling mixed-locale data sources where decimal separators (dots vs. commas) may vary.

**Tags:** `tag-manager` `variables` `data-types`
