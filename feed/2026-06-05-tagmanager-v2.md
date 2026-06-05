---
date: 2026-06-05
api: tagmanager.v2
service: Tag Manager
title: "Automatic decimal detection for variable conversion"
impact: low
breaking: false
tags: ["tag-manager", "variables", "data-types"]
interesting_score: 4
---

# Automatic decimal detection for variable conversion

**Date:** 2026-06-05  
**API:** `tagmanager.v2`  
**Impact:** Low  

## Summary

The Tag Manager API now supports automatic decimal separator detection when converting variable values to numbers.

## Details

A new enum value `automatic` has been added to the `convertToNumber` property within the `VariableFormatValue` schema. This allows for more robust programmatic configuration of variables, enabling the system to intelligently handle different decimal formats (like dots vs. commas) during numeric conversion without manual intervention.

**Tags:** `tag-manager` `variables` `data-types`
