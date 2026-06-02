---
date: 2026-06-02
api: tagmanager.v2
service: Tag Manager
title: "Automatic decimal detection for GTM variables"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Formatting"]
interesting_score: 4
---

# Automatic decimal detection for GTM variables

**Date:** 2026-06-02  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager now supports automatic decimal separator detection when converting variable values to numbers.

## Details

The VariableFormatValue schema has been updated with a new 'automatic' enum value for the convertToNumber property. This allows for more robust numeric conversions when dealing with internationalized data where decimal separators (dots vs. commas) may vary across different locales.

**Tags:** `Tag Manager` `Variables` `Data Formatting`
