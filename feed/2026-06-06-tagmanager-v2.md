---
date: 2026-06-06
api: tagmanager.v2
service: Tag Manager
title: "New Automatic Number Conversion for GTM Variables"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Processing"]
interesting_score: 4
---

# New Automatic Number Conversion for GTM Variables

**Date:** 2026-06-06  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager's API now supports automatic decimal separator detection when converting variable values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' enum value for the convertToNumber property. This allows developers to programmatically configure variables to handle numeric conversion more robustly by letting GTM detect the appropriate decimal separator automatically, reducing the need for manual locale-specific logic in tag configurations.

**Tags:** `Tag Manager` `Variables` `Data Processing`
