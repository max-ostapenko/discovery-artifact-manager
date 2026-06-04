---
date: 2026-06-04
api: tagmanager.v2
service: Google Tag Manager
title: "Automatic Decimal Detection for Variable Formatting"
impact: low
breaking: false
tags: ["tagmanager", "variables", "data-formatting"]
interesting_score: 4
---

# Automatic Decimal Detection for Variable Formatting

**Date:** 2026-06-04  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager's API now supports automatic decimal separator detection when converting variable values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' enum value for the convertToNumber property. This allows the Tag Manager engine to intelligently detect the decimal separator during conversion, which is particularly useful for handling internationalized data where separators may vary between dots and commas without requiring manual configuration for each locale.

**Tags:** `tagmanager` `variables` `data-formatting`
