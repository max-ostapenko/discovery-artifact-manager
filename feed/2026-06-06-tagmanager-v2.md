---
date: 2026-06-06
api: tagmanager.v2
service: Tag Manager
title: "Automatic Decimal Detection for Variable Formatting"
impact: low
breaking: false
tags: ["tag-manager", "variables", "data-formatting"]
interesting_score: 4
---

# Automatic Decimal Detection for Variable Formatting

**Date:** 2026-06-06  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager now supports automatic decimal separator detection when converting variable values to numbers via the API.

## Details

The `VariableFormatValue` schema has been updated to include a new `automatic` enum value for the `convertToNumber` property. This allows developers to format variables as numbers without manually specifying the decimal separator, which is a significant quality-of-life improvement for handling internationalized numeric strings where separators vary by locale.

**Tags:** `tag-manager` `variables` `data-formatting`
