---
date: 2026-06-17
api: tagmanager.v2
service: Google Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "containers"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-17  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has deprecated the get and link methods for container destinations, signaling a shift in how external tag destinations are managed.

## Details

The API discovery document now explicitly marks accounts.containers.destinations.get and accounts.containers.destinations.link as deprecated. This change suggests that the underlying 'destinations' resource is being phased out, likely in favor of newer Google Tag (gtag.js) management workflows or GA4-centric integrations.

**Tags:** `deprecation` `tag-manager` `containers`
