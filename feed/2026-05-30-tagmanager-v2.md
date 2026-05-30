---
date: 2026-05-30
api: tagmanager.v2
service: Google Tag Manager
title: "Automatic Decimal Detection for Variable Formatting"
impact: low
breaking: false
tags: ["tag-manager", "variables", "formatting"]
interesting_score: 4
---

# Automatic Decimal Detection for Variable Formatting

**Date:** 2026-05-30  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager's variable formatting now supports automatic decimal separator detection when converting values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' enum value for the convertToNumber property. This allows developers to convert string variables to numbers without manually specifying the decimal separator format, as the system will now attempt to detect it automatically during the conversion process.

**Tags:** `tag-manager` `variables` `formatting`
