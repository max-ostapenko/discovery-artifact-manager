---
date: 2026-06-05
api: tagmanager.v2
service: Google Tag Manager
title: "Automatic decimal detection for variable number conversion"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Transformation"]
interesting_score: 4
---

# Automatic decimal detection for variable number conversion

**Date:** 2026-06-05  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager variables now support an 'automatic' setting for number conversion, simplifying data formatting across different locales.

## Details

The `VariableFormatValue` schema has been updated to include a new `automatic` enum value for the `convertToNumber` property. This addition allows the API to automatically detect and handle decimal separators when transforming variable values into numeric formats, reducing the manual overhead of managing locale-specific number formatting in tag configurations.

**Tags:** `Tag Manager` `Variables` `Data Transformation`
