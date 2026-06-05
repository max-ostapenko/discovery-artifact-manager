---
date: 2026-06-05
api: tagmanager.v2
service: Tag Manager
title: "Automatic decimal detection for variable conversion"
impact: low
breaking: false
tags: ["tag-manager", "variables", "data-conversion"]
interesting_score: 4
---

# Automatic decimal detection for variable conversion

**Date:** 2026-06-05  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager now supports automatic decimal separator detection when converting variable values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' option within the convertToNumber enum. This allows for more robust conversion of string-based variables into numbers by automatically detecting the decimal separator, which is particularly useful when dealing with internationalized data formats where separators vary between dots and commas.

**Tags:** `tag-manager` `variables` `data-conversion`
