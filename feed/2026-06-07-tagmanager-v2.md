---
date: 2026-06-07
api: tagmanager.v2
service: Tag Manager
title: "Automatic Number Conversion Added to Variables"
impact: low
breaking: false
tags: ["tag-manager", "variables", "data-normalization"]
interesting_score: 4
---

# Automatic Number Conversion Added to Variables

**Date:** 2026-06-07  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager now supports automatic decimal separator detection when converting variable values to numbers.

## Details

The `VariableFormatValue` schema has been updated to include a new enum value, `automatic`, for the `convertToNumber` property. This addition allows the API to automatically detect the correct decimal separator during type conversion, which is particularly useful for handling internationalized data formats without manual regex or logic.

**Tags:** `tag-manager` `variables` `data-normalization`
