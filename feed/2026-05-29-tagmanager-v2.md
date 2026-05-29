---
date: 2026-05-29
api: tagmanager.v2
service: Tag Manager
title: "Automatic Number Conversion in Tag Manager Variables"
impact: low
breaking: false
tags: ["tag-manager", "variables", "data-types"]
interesting_score: 4
---

# Automatic Number Conversion in Tag Manager Variables

**Date:** 2026-05-29  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager now supports automatic decimal separator detection when converting variable values to numbers.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' option for the convertToNumber property. This allows the API to handle numeric conversion more flexibly by detecting the appropriate decimal separator automatically, which is particularly useful for handling international number formats without manual configuration.

**Tags:** `tag-manager` `variables` `data-types`
