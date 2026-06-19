---
date: 2026-06-19
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-19  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for container destinations, signaling a shift away from these specific management endpoints.

## Details

The discovery document for tagmanager.v2 now marks accounts.containers.destinations.get and accounts.containers.destinations.link with a deprecated flag. While these methods are still currently available, developers should begin auditing their implementations to move away from these endpoints as they are no longer recommended for new integrations.

**Tags:** `deprecation` `tag-manager`
