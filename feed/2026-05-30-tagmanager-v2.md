---
date: 2026-05-30
api: tagmanager.v2
service: Tag Manager
title: "Automatic decimal detection for GTM variables"
impact: low
breaking: false
tags: ["tag-manager", "variables", "formatting"]
interesting_score: 4
---

# Automatic decimal detection for GTM variables

**Date:** 2026-05-30  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager now supports automatic decimal separator detection when converting variable values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' option for the convertToNumber property. This allows for more robust numeric conversions across different locales by automatically detecting the decimal separator used in the input string.

**Tags:** `tag-manager` `variables` `formatting`
