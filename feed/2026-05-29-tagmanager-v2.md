---
date: 2026-05-29
api: tagmanager.v2
service: Google Tag Manager
title: "Automatic decimal detection for variable number conversion"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Formatting"]
interesting_score: 4
---

# Automatic decimal detection for variable number conversion

**Date:** 2026-05-29  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager variables now support automatic decimal separator detection when converting values to numbers.

## Details

The `VariableFormatValue` schema has been updated to include a new `automatic` option within the `convertToNumber` enum. This allows developers to programmatically configure variables to handle numeric conversion more robustly by automatically detecting whether a dot or comma is used as the decimal separator in the input string.

**Tags:** `Tag Manager` `Variables` `Data Formatting`
