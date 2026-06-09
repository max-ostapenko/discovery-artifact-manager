---
date: 2026-06-09
api: tagmanager.v2
service: Tag Manager
title: "Automatic decimal detection for variable conversion"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Formatting"]
interesting_score: 4
---

# Automatic decimal detection for variable conversion

**Date:** 2026-06-09  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager variables now support automatic decimal separator detection when converting values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new "automatic" option for the convertToNumber property. This allows the API to handle numeric conversions more intelligently by detecting the appropriate decimal separator, which is particularly useful for handling internationalized data formats where separators (like commas vs. dots) vary by locale.

**Tags:** `Tag Manager` `Variables` `Data Formatting`
