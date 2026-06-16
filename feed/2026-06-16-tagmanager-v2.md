---
date: 2026-06-16
api: tagmanager.v2
service: Google Tag Manager
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

Google Tag Manager has officially deprecated the 'get' and 'link' methods for container destinations, signaling a shift in how tag destinations are managed.

## Details

The methods accounts.containers.destinations.get and accounts.containers.destinations.link have been marked as deprecated in the discovery document. This affects developers programmatically managing GA4 or server-side tagging destinations. While the methods remain functional for now, you should begin auditing your scripts and looking for alternative configuration paths in the GTM API.

**Tags:** `deprecation` `tag-manager` `automation`
