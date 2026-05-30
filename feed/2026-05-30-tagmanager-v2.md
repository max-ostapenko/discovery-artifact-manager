---
date: 2026-05-30
api: tagmanager.v2
service: Google Tag Manager
title: "Automatic decimal detection for variable conversion"
impact: low
breaking: false
tags: ["tag-manager", "variables", "data-processing"]
interesting_score: 4
---

# Automatic decimal detection for variable conversion

**Date:** 2026-05-30  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager variables now support automatic decimal separator detection when converting values to numbers.

## Details

The `VariableFormatValue` schema adds a new `automatic` option to the `convertToNumber` enum. This allows the API to automatically detect the decimal separator (like dots vs. commas) when transforming variable strings into numeric types. This is particularly useful for developers handling internationalized data sources who previously had to write custom JavaScript to normalize numeric formats.

**Tags:** `tag-manager` `variables` `data-processing`
