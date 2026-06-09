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

Google Tag Manager now supports automatic decimal separator detection when converting variable values to numbers.

## Details

The VariableFormatValue schema's convertToNumber property has been updated with a new enum value: 'automatic'. This addition allows the API to intelligently detect decimal separators during number conversion, which is particularly useful for handling localized numeric strings (e.g., switching between dots and commas) without requiring custom transformation logic.

**Tags:** `Tag Manager` `Variables` `Data Formatting`
