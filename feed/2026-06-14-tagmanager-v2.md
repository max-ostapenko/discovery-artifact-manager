---
date: 2026-06-14
api: tagmanager.v2
service: Google Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["tagmanager", "deprecation", "analytics"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-14  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially marked the 'get' and 'link' methods for Container Destinations as deprecated.

## Details

The API discovery document now flags 'accounts.containers.destinations.get' and 'accounts.containers.destinations.link' with a deprecated status. Developers currently using these methods to manage destination links—typically used in server-side tagging or GA4 configurations—should begin looking for alternative workflows as these methods are likely slated for eventual removal.

**Tags:** `tagmanager` `deprecation` `analytics`
