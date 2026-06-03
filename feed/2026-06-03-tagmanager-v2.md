---
date: 2026-06-03
api: tagmanager.v2
service: Tag Manager
title: "New Automatic Number Conversion in Tag Manager"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Formatting"]
interesting_score: 4
---

# New Automatic Number Conversion in Tag Manager

**Date:** 2026-06-03  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager's VariableFormatValue now supports an 'automatic' option for number conversion, simplifying decimal separator handling.

## Details

The VariableFormatValue schema has been updated to include a new enum value 'automatic' for the convertToNumber property. This allows developers to convert variable values to numbers while letting the system automatically detect the appropriate decimal separator, which is particularly useful when dealing with internationalized data where separators vary by locale.

**Tags:** `Tag Manager` `Variables` `Data Formatting`
