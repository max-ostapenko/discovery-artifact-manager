---
date: 2026-05-29
api: tagmanager.v2
service: Google Tag Manager
title: "New Automatic Number Conversion for GTM Variables"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Formatting"]
interesting_score: 4
---

# New Automatic Number Conversion for GTM Variables

**Date:** 2026-05-29  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager now supports automatic decimal separator detection when converting variable values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' enum value for the convertToNumber property. This allows developers to transform variable strings into numbers without manually specifying the decimal format, which is particularly useful for handling internationalized data formats where separators (commas vs. dots) vary by locale.

**Tags:** `Tag Manager` `Variables` `Data Formatting`
