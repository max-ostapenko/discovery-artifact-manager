---
date: 2026-05-31
api: tagmanager.v2
service: Tag Manager
title: "Automatic Decimal Detection for Variable Formatting"
impact: low
breaking: false
tags: ["tag-manager", "variables", "data-types"]
interesting_score: 4
---

# Automatic Decimal Detection for Variable Formatting

**Date:** 2026-05-31  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager now supports automatic decimal separator detection when converting variable values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' option for the convertToNumber property. This allows the API to intelligently handle different decimal separators (such as dots or commas) during type conversion, which is particularly useful for handling internationalized data formats without manual pre-processing.

**Tags:** `tag-manager` `variables` `data-types`
