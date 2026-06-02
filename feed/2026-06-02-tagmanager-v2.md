---
date: 2026-06-02
api: tagmanager.v2
service: Tag Manager
title: "Automatic decimal detection for variable conversion"
impact: low
breaking: false
tags: ["tag-manager", "variables", "formatting"]
interesting_score: 4
---

# Automatic decimal detection for variable conversion

**Date:** 2026-06-02  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager's API now supports automatic decimal separator detection when converting variables to numbers.

## Details

A new enum value 'automatic' has been added to the 'convertToNumber' property within the VariableFormatValue schema. This allows developers to format variables as numbers without manually specifying the decimal separator format, as the system will now attempt to detect it automatically, simplifying data processing for internationalized inputs.

**Tags:** `tag-manager` `variables` `formatting`
