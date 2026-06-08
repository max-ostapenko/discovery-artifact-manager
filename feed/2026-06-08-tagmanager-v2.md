---
date: 2026-06-08
api: tagmanager.v2
service: Google Tag Manager
title: "Automatic Number Conversion for GTM Variables"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Types"]
interesting_score: 4
---

# Automatic Number Conversion for GTM Variables

**Date:** 2026-06-08  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager now supports automatic decimal separator detection when converting variable values to numbers.

## Details

The `VariableFormatValue` schema has been updated to include a new `automatic` enum value for the `convertToNumber` property. This addition allows the API to automatically detect decimal separators during type conversion, which is particularly useful for handling numeric data from diverse locales without manual parsing logic.

**Tags:** `Tag Manager` `Variables` `Data Types`
