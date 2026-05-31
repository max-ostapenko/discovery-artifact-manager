---
date: 2026-05-31
api: tagmanager.v2
service: Tag Manager
title: "Automatic decimal detection for variable conversion"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Formatting"]
interesting_score: 4
---

# Automatic decimal detection for variable conversion

**Date:** 2026-05-31  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager variables now support automatic decimal separator detection when converting values to numbers.

## Details

The `VariableFormatValue` schema has been updated to include a new `automatic` enum value within the `convertToNumber` property. This addition allows developers and marketers to convert string variables to numbers without manually specifying the decimal format, which is particularly useful for handling internationalized data where separators (dots vs. commas) vary by locale.

**Tags:** `Tag Manager` `Variables` `Data Formatting`
