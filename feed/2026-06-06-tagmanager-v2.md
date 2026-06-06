---
date: 2026-06-06
api: tagmanager.v2
service: Google Tag Manager
title: "Automatic decimal detection for variable conversion"
impact: low
breaking: false
tags: ["tagmanager", "variables", "data-conversion"]
interesting_score: 4
---

# Automatic decimal detection for variable conversion

**Date:** 2026-06-06  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager's VariableFormatValue now supports automatic decimal separator detection when converting variables to numbers.

## Details

The `convertToNumber` property within the `VariableFormatValue` schema has been expanded with a new enum value: `automatic`. This allows the API to handle numeric conversion more intelligently by detecting the decimal separator automatically, which is particularly useful for processing data from diverse locales without manual formatting logic.

**Tags:** `tagmanager` `variables` `data-conversion`
