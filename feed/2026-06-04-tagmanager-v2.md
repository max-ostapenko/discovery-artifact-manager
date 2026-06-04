---
date: 2026-06-04
api: tagmanager.v2
service: Tag Manager
title: "Automatic Number Conversion for GTM Variables"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Transformation"]
interesting_score: 4
---

# Automatic Number Conversion for GTM Variables

**Date:** 2026-06-04  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager variables now support automatic decimal separator detection during number conversion.

## Details

The `VariableFormatValue` schema has been updated to include a new `automatic` option for the `convertToNumber` property. This allows the API to handle numeric string conversions by automatically detecting the decimal separator, which simplifies processing data from diverse locales without manual format configuration.

**Tags:** `Tag Manager` `Variables` `Data Transformation`
