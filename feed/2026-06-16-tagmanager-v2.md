---
date: 2026-06-16
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "automation"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-16  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for container destinations. Developers using these endpoints for automation should begin planning for alternative workflows.

## Details

The discovery document now explicitly flags 'accounts.containers.destinations.get' and 'accounts.containers.destinations.link' as deprecated. This change signals a shift in how GTM handles destination resources, likely moving toward a different integration model for GA4 or server-side tagging configurations.

**Tags:** `deprecation` `tag-manager` `automation`
