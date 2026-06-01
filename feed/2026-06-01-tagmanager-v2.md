---
date: 2026-06-01
api: tagmanager.v2
service: Google Tag Manager
title: "Automatic Decimal Detection for Variable Conversion"
impact: low
breaking: false
tags: ["tag-manager", "variables", "data-formatting"]
interesting_score: 4
---

# Automatic Decimal Detection for Variable Conversion

**Date:** 2026-06-01  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager variables now support automatic decimal separator detection when converting values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' enum value for the convertToNumber property. This addition allows the API to intelligently handle different decimal separators (like dots vs. commas) during number conversion, which is particularly useful for processing internationalized data inputs without manual formatting logic.

**Tags:** `tag-manager` `variables` `data-formatting`
