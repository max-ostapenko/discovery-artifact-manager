---
date: 2026-06-18
api: tagmanager.v2
service: Google Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-18  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has deprecated the get and link methods for container destinations, signaling a shift in how external destinations are managed.

## Details

The API discovery document now explicitly marks the `accounts.containers.destinations.get` and `accounts.containers.destinations.link` methods as deprecated. This change suggests that developers should begin looking for alternative ways to manage container destinations, likely through the unified Google Tag (gtag.js) integrations, as these specific endpoints may be removed in a future revision.

**Tags:** `deprecation` `tag-manager`
