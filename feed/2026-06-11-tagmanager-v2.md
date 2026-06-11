---
date: 2026-06-11
api: tagmanager.v2
service: Google Tag Manager
title: "GTM Container Destinations methods deprecated"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager"]
interesting_score: 5
---

# GTM Container Destinations methods deprecated

**Date:** 2026-06-11  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

The `get` and `link` methods for Tag Manager container destinations are now officially deprecated.

## Details

Google Tag Manager is signaling a shift away from the current destinations management pattern. The `accounts.containers.destinations.get` and `accounts.containers.destinations.link` methods have been marked as deprecated in the discovery document. Developers currently relying on these methods for linking or retrieving destination configurations should prepare for future API changes or migration to newer resource types.

**Tags:** `deprecation` `tag-manager`
