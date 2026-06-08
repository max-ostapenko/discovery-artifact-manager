---
date: 2026-06-08
api: tagmanager.v2
service: Google Tag Manager
title: "Automatic Decimal Detection for Variable Formatting"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Formatting"]
interesting_score: 4
---

# Automatic Decimal Detection for Variable Formatting

**Date:** 2026-06-08  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager variables now support automatic decimal separator detection when converting values to numbers.

## Details

The `VariableFormatValue` schema has been updated to include a new `automatic` enum value for the `convertToNumber` property. This addition allows the Tag Manager engine to automatically detect and handle different decimal separators during numeric conversion, simplifying data processing for internationalized inputs where comma vs. dot separators might vary.

**Tags:** `Tag Manager` `Variables` `Data Formatting`
