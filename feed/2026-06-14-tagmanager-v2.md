---
date: 2026-06-14
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "containers"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-14  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the get and link methods for container destinations. Developers should begin auditing their integrations to move away from these endpoints.

## Details

The discovery document now explicitly flags accounts.containers.destinations.get and accounts.containers.destinations.link as deprecated. While these methods remain functional for now, their deprecation suggests a shift in how GTM handles destination resources, and they may be removed or replaced in a future API revision.

**Tags:** `deprecation` `tag-manager` `containers`
