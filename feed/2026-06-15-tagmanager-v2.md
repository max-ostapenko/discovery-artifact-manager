---
date: 2026-06-15
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "automation"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-15  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for container destinations. Developers using these endpoints for destination management should begin planning for their eventual removal.

## Details

The discovery document now explicitly marks the 'accounts.containers.destinations.get' and 'accounts.containers.destinations.link' methods as deprecated. This change signals a shift in how Tag Manager handles destination configurations, likely favoring newer integration patterns or unified tagging schemas.

**Tags:** `deprecation` `tag-manager` `automation`
