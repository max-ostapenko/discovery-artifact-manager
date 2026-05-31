---
date: 2026-05-31
api: tagmanager.v2
service: Google Tag Manager
title: "Automatic Decimal Detection for Variable Number Conversion"
impact: low
breaking: false
tags: ["tag-manager", "variables", "data-transformation"]
interesting_score: 4
---

# Automatic Decimal Detection for Variable Number Conversion

**Date:** 2026-05-31  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager's variable formatting now supports automatic decimal separator detection when converting values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' enum value for the convertToNumber property. This allows the API to intelligently handle different decimal separators (such as dots or commas) when transforming variable strings into numeric types, which is particularly useful for handling internationalized data formats without custom scripts.

**Tags:** `tag-manager` `variables` `data-transformation`
