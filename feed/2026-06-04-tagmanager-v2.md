---
date: 2026-06-04
api: tagmanager.v2
service: Google Tag Manager
title: "New Automatic Number Conversion for GTM Variables"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Types"]
interesting_score: 4
---

# New Automatic Number Conversion for GTM Variables

**Date:** 2026-06-04  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager now supports automatic decimal separator detection when converting variable values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' enum value for the convertToNumber property. This allows the API to handle various decimal formats automatically during conversion, which is particularly useful for developers dealing with internationalized data where decimal separators (dots vs. commas) vary by locale.

**Tags:** `Tag Manager` `Variables` `Data Types`
