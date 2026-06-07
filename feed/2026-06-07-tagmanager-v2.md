---
date: 2026-06-07
api: tagmanager.v2
service: Google Tag Manager
title: "Automatic Decimal Detection for Variable Conversion"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Formatting"]
interesting_score: 4
---

# Automatic Decimal Detection for Variable Conversion

**Date:** 2026-06-07  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Tag Manager variables now support automatic decimal separator detection when converting values to numbers.

## Details

The `VariableFormatValue` schema has been updated to include a new `automatic` enum value for the `convertToNumber` property. This allows developers to convert variable values to numbers without manually specifying the decimal format, which is particularly useful for handling internationalized numeric strings where separators vary by locale.

**Tags:** `Tag Manager` `Variables` `Data Formatting`
