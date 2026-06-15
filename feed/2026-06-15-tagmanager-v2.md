---
date: 2026-06-15
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-15  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the get and link methods for container destinations, signaling a shift in how destinations are managed.

## Details

The discovery document now explicitly marks the 'get' and 'link' methods within the 'accounts.containers.destinations' resource as deprecated. While these methods currently remain functional, developers should begin auditing their codebases to reduce reliance on these specific endpoints for managing GTM destinations.

**Tags:** `deprecation` `tag-manager` `api-lifecycle`
