---
date: 2026-05-29
api: tagmanager.v2
service: Google Tag Manager
title: "Automatic Decimal Detection for Variable Conversion"
impact: low
breaking: false
tags: ["tag-manager", "variables", "data-transformation"]
interesting_score: 4
---

# Automatic Decimal Detection for Variable Conversion

**Date:** 2026-05-29  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager variables now support automatic decimal separator detection when converting values to numbers.

## Details

A new 'automatic' enum value has been added to the VariableFormatValue.convertToNumber property. This allows the API to handle numeric string conversions by automatically detecting the decimal separator, which is particularly useful for handling internationalized data where dots and commas are used interchangeably as separators.

**Tags:** `tag-manager` `variables` `data-transformation`
