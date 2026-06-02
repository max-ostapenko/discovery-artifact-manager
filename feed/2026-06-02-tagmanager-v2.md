---
date: 2026-06-02
api: tagmanager.v2
service: Tag Manager
title: "Automatic decimal detection for number conversion"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Transformation"]
interesting_score: 4
---

# Automatic decimal detection for number conversion

**Date:** 2026-06-02  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager variables now support automatic decimal separator detection when converting values to numbers.

## Details

The VariableFormatValue schema has been updated to include an 'automatic' enum value for the convertToNumber property. This allows the Tag Manager engine to intelligently detect decimal separators during variable formatting, which is particularly useful when processing internationalized data where separators might vary between dots and commas without requiring custom JavaScript logic.

**Tags:** `Tag Manager` `Variables` `Data Transformation`
