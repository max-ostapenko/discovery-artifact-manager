---
date: 2026-06-02
api: tagmanager.v2
service: Google Tag Manager
title: "Automatic Decimal Detection for Variable Number Conversion"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Casting"]
interesting_score: 4
---

# Automatic Decimal Detection for Variable Number Conversion

**Date:** 2026-06-02  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager variables now support automatic decimal separator detection when converting values to numbers.

## Details

The `VariableFormatValue` schema has been updated to include a new `automatic` enum value for the `convertToNumber` property. This addition allows the API to handle numeric casting with automatic detection of decimal separators, simplifying data processing for internationalized input strings where separators (like commas vs. periods) may vary.

**Tags:** `Tag Manager` `Variables` `Data Casting`
