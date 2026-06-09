---
date: 2026-06-09
api: tagmanager.v2
service: Tag Manager
title: "Automatic decimal detection for variable conversion"
impact: low
breaking: false
tags: ["tagmanager", "variables", "formatting"]
interesting_score: 4
---

# Automatic decimal detection for variable conversion

**Date:** 2026-06-09  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager's variable formatting now supports automatic decimal separator detection when converting values to numbers.

## Details

The VariableFormatValue schema's convertToNumber property has been updated with a new enum value: 'automatic'. This allows developers to convert variable values to numbers without manually specifying the decimal separator, which is particularly useful for handling internationalized number formats where separators vary by locale.

**Tags:** `tagmanager` `variables` `formatting`
