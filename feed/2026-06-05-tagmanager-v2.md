---
date: 2026-06-05
api: tagmanager.v2
service: Google Tag Manager
title: "Automatic Decimal Detection for Variable Formatting"
impact: low
breaking: false
tags: ["tagmanager", "variables", "automation"]
interesting_score: 4
---

# Automatic Decimal Detection for Variable Formatting

**Date:** 2026-06-05  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

Google Tag Manager now supports automatic decimal separator detection when converting variable values to numbers via the API.

## Details

The VariableFormatValue schema has been updated to include a new 'automatic' enum value for the convertToNumber property. This allows developers programmatically managing GTM configurations to enable numeric conversion that automatically detects the appropriate decimal separator, simplifying data processing for localized or internationalized inputs.

**Tags:** `tagmanager` `variables` `automation`
