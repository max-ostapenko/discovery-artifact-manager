---
date: 2026-06-06
api: tagmanager.v2
service: Tag Manager
title: "Automatic decimal detection for variable number conversion"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Transformation"]
interesting_score: 4
---

# Automatic decimal detection for variable number conversion

**Date:** 2026-06-06  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager now supports automatic decimal separator detection when converting variable values to numbers.

## Details

A new enum value, `automatic`, has been added to the `convertToNumber` property within the `VariableFormatValue` schema. This allows developers and tag managers to handle numeric strings from diverse locales more robustly by letting the system detect whether a dot or comma is being used as the decimal separator.

**Tags:** `Tag Manager` `Variables` `Data Transformation`
