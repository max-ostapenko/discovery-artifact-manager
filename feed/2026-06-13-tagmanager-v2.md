---
date: 2026-06-13
api: tagmanager.v2
service: Google Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["tagmanager", "deprecation", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-13  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for container destinations, signaling a shift in how tag destinations are managed.

## Details

The discovery document now marks 'accounts.containers.destinations.get' and 'accounts.containers.destinations.link' as deprecated. Developers currently relying on these methods to retrieve or link destinations within GTM containers should begin auditing their implementations and look for alternative configuration paths, as these endpoints are likely slated for eventual removal.

**Tags:** `tagmanager` `deprecation` `api-lifecycle`
