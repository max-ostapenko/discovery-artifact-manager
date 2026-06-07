---
date: 2026-06-07
api: tagmanager.v2
service: Tag Manager
title: "Automatic decimal detection for variable conversion"
impact: low
breaking: false
tags: ["tag-manager", "variables", "data-formatting"]
interesting_score: 4
---

# Automatic decimal detection for variable conversion

**Date:** 2026-06-07  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager variables now support automatic decimal separator detection when converting values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' option within the convertToNumber enum. This allows for more flexible data ingestion by automatically detecting the appropriate decimal separator during string-to-number conversion, reducing the need for custom parsing logic when dealing with internationalized numeric formats.

**Tags:** `tag-manager` `variables` `data-formatting`
