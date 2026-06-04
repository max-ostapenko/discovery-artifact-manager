---
date: 2026-06-04
api: tagmanager.v2
service: Tag Manager
title: "Automatic decimal detection for variable conversion"
impact: low
breaking: false
tags: ["tag-manager", "variables", "formatting"]
interesting_score: 4
---

# Automatic decimal detection for variable conversion

**Date:** 2026-06-04  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager variables now support automatic decimal separator detection when converting values to numbers.

## Details

A new 'automatic' enum value has been added to the convertToNumber property within the VariableFormatValue schema. This allows developers to transform variable strings into numbers without manually specifying the decimal format, which is particularly useful for handling localized numeric strings from different regions.

**Tags:** `tag-manager` `variables` `formatting`
