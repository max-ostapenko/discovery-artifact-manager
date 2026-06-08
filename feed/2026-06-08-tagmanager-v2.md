---
date: 2026-06-08
api: tagmanager.v2
service: Tag Manager
title: "Automatic decimal detection for GTM variables"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Normalization"]
interesting_score: 4
---

# Automatic decimal detection for GTM variables

**Date:** 2026-06-08  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager's VariableFormatValue now supports an 'automatic' option for number conversion, simplifying data normalization across different locales.

## Details

The VariableFormatValue schema has been updated to include a new enum value 'automatic' for the convertToNumber property. This allows developers to convert variable values to numbers without manually specifying the decimal separator, as the system will now attempt to detect it automatically based on the input string.

**Tags:** `Tag Manager` `Variables` `Data Normalization`
