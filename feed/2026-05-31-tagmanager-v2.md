---
date: 2026-05-31
api: tagmanager.v2
service: Tag Manager
title: "Automatic decimal detection for variable conversion"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Transformation"]
interesting_score: 4
---

# Automatic decimal detection for variable conversion

**Date:** 2026-05-31  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager's variable formatting now supports automatic decimal separator detection when converting values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' enum value for the convertToNumber property. This allows the API to intelligently detect the decimal separator during type conversion, which is particularly useful for handling international number formats (e.g., commas vs. periods) without requiring custom transformation logic or regex.

**Tags:** `Tag Manager` `Variables` `Data Transformation`
