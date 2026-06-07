---
date: 2026-06-07
api: tagmanager.v2
service: Tag Manager
title: "New Automatic Number Conversion for GTM Variables"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Processing"]
interesting_score: 4
---

# New Automatic Number Conversion for GTM Variables

**Date:** 2026-06-07  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager's VariableFormatValue schema now supports automatic decimal separator detection when converting variables to numbers.

## Details

A new enum value 'automatic' has been added to the convertToNumber property within the VariableFormatValue schema. This allows developers to handle numeric conversions more robustly by letting the system detect the appropriate decimal separator automatically, which is particularly useful when dealing with localized data formats that vary between periods and commas.

**Tags:** `Tag Manager` `Variables` `Data Processing`
