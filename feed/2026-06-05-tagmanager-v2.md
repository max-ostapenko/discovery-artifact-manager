---
date: 2026-06-05
api: tagmanager.v2
service: Tag Manager
title: "New Automatic Number Conversion in Tag Manager Variables"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Formatting"]
interesting_score: 4
---

# New Automatic Number Conversion in Tag Manager Variables

**Date:** 2026-06-05  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager API now supports automatic decimal separator detection when converting variable values to numbers.

## Details

A new enum value 'automatic' has been added to the 'convertToNumber' property within the 'VariableFormatValue' schema. This allows developers to programmatically configure variables to handle numeric conversion more robustly, specifically by letting GTM automatically detect the appropriate decimal separator, which is particularly useful for handling internationalized numeric strings.

**Tags:** `Tag Manager` `Variables` `Data Formatting`
