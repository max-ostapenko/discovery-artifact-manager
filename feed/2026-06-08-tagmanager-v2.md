---
date: 2026-06-08
api: tagmanager.v2
service: Tag Manager
title: "New Automatic Number Conversion for GTM Variables"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Normalization"]
interesting_score: 4
---

# New Automatic Number Conversion for GTM Variables

**Date:** 2026-06-08  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager now supports automatic decimal separator detection when converting variable values to numbers.

## Details

A new enum value 'automatic' has been added to the 'convertToNumber' property within the VariableFormatValue schema. This enhancement allows the API to automatically detect decimal separators when transforming variable strings into numeric types, reducing the need for manual locale-specific parsing logic.

**Tags:** `Tag Manager` `Variables` `Data Normalization`
