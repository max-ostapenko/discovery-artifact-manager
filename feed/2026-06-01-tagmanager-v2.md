---
date: 2026-06-01
api: tagmanager.v2
service: Tag Manager
title: "Automatic decimal detection for variable conversion"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Formatting"]
interesting_score: 4
---

# Automatic decimal detection for variable conversion

**Date:** 2026-06-01  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager now supports automatic decimal separator detection when converting variable values to numbers.

## Details

The `VariableFormatValue` schema has been updated to include a new `automatic` enum value for the `convertToNumber` property. This allows developers to trigger numeric conversion that intelligently handles different decimal separator formats without manual configuration.

**Tags:** `Tag Manager` `Variables` `Data Formatting`
