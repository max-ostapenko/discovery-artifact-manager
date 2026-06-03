---
date: 2026-06-03
api: tagmanager.v2
service: Google Tag Manager
title: "Automatic Decimal Detection for Variable Formatting"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Formatting"]
interesting_score: 4
---

# Automatic Decimal Detection for Variable Formatting

**Date:** 2026-06-03  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager variables now support automatic decimal separator detection when converting values to numbers.

## Details

The `VariableFormatValue` schema has been updated to include a new enum value, `automatic`, for the `convertToNumber` property. This allows developers and marketers to convert variable strings to numbers without manually specifying the decimal separator, which is particularly useful for handling internationalized data where dots and commas are used interchangeably as separators.

**Tags:** `Tag Manager` `Variables` `Data Formatting`
