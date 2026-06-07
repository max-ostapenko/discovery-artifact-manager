---
date: 2026-06-07
api: tagmanager.v2
service: Tag Manager
title: "New Automatic Number Conversion for GTM Variables"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Transformation"]
interesting_score: 4
---

# New Automatic Number Conversion for GTM Variables

**Date:** 2026-06-07  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

The Tag Manager API now supports automatic decimal separator detection when converting variable values to numbers.

## Details

A new enum value 'automatic' has been added to the 'convertToNumber' property within the 'VariableFormatValue' schema. This allows developers to programmatically configure variables to handle numeric conversion more robustly, specifically by letting GTM automatically detect the appropriate decimal separator based on the input string.

**Tags:** `Tag Manager` `Variables` `Data Transformation`
