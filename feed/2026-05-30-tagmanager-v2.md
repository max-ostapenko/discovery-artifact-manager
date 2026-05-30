---
date: 2026-05-30
api: tagmanager.v2
service: Tag Manager
title: "Automatic decimal detection for variable conversion"
impact: low
breaking: false
tags: ["tag-manager", "variables", "data-processing"]
interesting_score: 4
---

# Automatic decimal detection for variable conversion

**Date:** 2026-05-30  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager variables now support automatic decimal separator detection when converting values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' enum value for the convertToNumber property. This allows developers to programmatically configure variables to handle numeric conversion without manually specifying the decimal separator format, which is useful for processing internationalized data streams.

**Tags:** `tag-manager` `variables` `data-processing`
