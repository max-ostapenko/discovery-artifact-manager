---
date: 2026-06-20
api: tagmanager.v2
service: Google Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["tag-manager", "deprecation", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-20  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

The 'get' and 'link' methods for Tag Manager container destinations have been officially marked as deprecated.

## Details

The API discovery document now flags 'accounts.containers.destinations.get' and 'accounts.containers.destinations.link' with a deprecated status. While these methods remain functional for the time being, developers should prepare for a transition and avoid building new logic around these specific endpoints for managing container destinations.

**Tags:** `tag-manager` `deprecation` `api-lifecycle`
