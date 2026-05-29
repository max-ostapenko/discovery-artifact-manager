---
date: 2026-05-29
api: tagmanager.v2
service: Tag Manager
title: "Automatic Decimal Detection for Variable Conversions"
impact: low
breaking: false
tags: ["Tag Manager", "Variables", "Data Formatting"]
interesting_score: 4
---

# Automatic Decimal Detection for Variable Conversions

**Date:** 2026-05-29  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

The Tag Manager API now supports automatic decimal separator detection when converting variable values to numbers.

## Details

A new 'automatic' enum value has been added to the `convertToNumber` property within the `VariableFormatValue` schema. This allows developers to programmatically configure variables to intelligently handle numeric conversions without manually specifying decimal formats, which is particularly useful for handling internationalized data streams.

**Tags:** `Tag Manager` `Variables` `Data Formatting`
