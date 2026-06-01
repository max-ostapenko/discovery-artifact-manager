---
date: 2026-06-01
api: tagmanager.v2
service: Google Tag Manager
title: "Automatic Decimal Detection for Variable Number Conversion"
impact: low
breaking: false
tags: ["tag-manager", "variables", "data-transformation"]
interesting_score: 4
---

# Automatic Decimal Detection for Variable Number Conversion

**Date:** 2026-06-01  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager now supports automatic decimal separator detection when converting variable values to numbers, simplifying internationalized data handling.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' enum value for the convertToNumber property. This allows the Tag Manager API to intelligently detect the correct decimal separator when transforming string-based variables into numeric types, which is particularly useful for handling diverse locale-specific number formats without manual string manipulation.

**Tags:** `tag-manager` `variables` `data-transformation`
