---
date: 2026-06-04
api: tagmanager.v2
service: Google Tag Manager
title: "New Automatic Number Conversion for GTM Variables"
impact: low
breaking: false
tags: ["tag-manager", "variables", "data-formatting"]
interesting_score: 4
---

# New Automatic Number Conversion for GTM Variables

**Date:** 2026-06-04  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager variables now support automatic decimal separator detection when converting values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' option for the convertToNumber property. This allows for more robust conversion of string-based variables into numeric types by automatically detecting the decimal separator, which is useful when dealing with internationalized data formats.

**Tags:** `tag-manager` `variables` `data-formatting`
