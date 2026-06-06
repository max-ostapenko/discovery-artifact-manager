---
date: 2026-06-06
api: tagmanager.v2
service: Google Tag Manager
title: "Automatic decimal detection for GTM variables"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Formatting"]
interesting_score: 4
---

# Automatic decimal detection for GTM variables

**Date:** 2026-06-06  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager's API now supports automatic decimal separator detection when converting variable values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' enum value for the convertToNumber property. This allows the Tag Manager engine to automatically detect the appropriate decimal separator when parsing strings into numbers, which is particularly useful for handling internationalized data inputs where separators (commas vs. dots) may vary.

**Tags:** `Tag Manager` `Variables` `Data Formatting`
