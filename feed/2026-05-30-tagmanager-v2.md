---
date: 2026-05-30
api: tagmanager.v2
service: Tag Manager
title: "GTM Variables get automatic decimal detection"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Formatting"]
interesting_score: 4
---

# GTM Variables get automatic decimal detection

**Date:** 2026-05-30  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager's variable formatting now supports automatic decimal separator detection when converting values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' enum value for the convertToNumber property. This allows for more robust numeric conversions in environments where decimal separators (dots vs. commas) vary by locale or data source.

**Tags:** `Tag Manager` `Variables` `Data Formatting`
