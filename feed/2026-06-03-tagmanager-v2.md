---
date: 2026-06-03
api: tagmanager.v2
service: Tag Manager
title: "Automatic decimal detection for GTM variables"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Formatting"]
interesting_score: 4
---

# Automatic decimal detection for GTM variables

**Date:** 2026-06-03  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager's VariableFormatValue now supports automatic decimal separator detection when converting variable values to numbers.

## Details

The `convertToNumber` property within the `VariableFormatValue` schema has been updated with a new enum value: `automatic`. This addition allows the API to handle numeric strings with varying decimal formats automatically, which is particularly useful for developers handling internationalized data where decimal separators (dots vs. commas) vary by locale.

**Tags:** `Tag Manager` `Variables` `Data Formatting`
