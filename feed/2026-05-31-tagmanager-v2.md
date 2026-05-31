---
date: 2026-05-31
api: tagmanager.v2
service: Google Tag Manager
title: "Automatic number conversion for GTM variables"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Formatting"]
interesting_score: 4
---

# Automatic number conversion for GTM variables

**Date:** 2026-05-31  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager variables now support automatic decimal separator detection when converting values to numbers.

## Details

The `VariableFormatValue` schema has been updated to include a new `automatic` enum value for the `convertToNumber` property. This allows the API to handle numeric conversions more intelligently by detecting the appropriate decimal separator based on the input string, simplifying data processing for internationalized sites.

**Tags:** `Tag Manager` `Variables` `Data Formatting`
