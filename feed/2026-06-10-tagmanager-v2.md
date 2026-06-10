---
date: 2026-06-10
api: tagmanager.v2
service: Google Tag Manager
title: "Deprecation of Container Destination Methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "containers"]
interesting_score: 5
---

# Deprecation of Container Destination Methods

**Date:** 2026-06-10  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for container destinations, signaling a shift in how tagging destinations are managed.

## Details

The discovery document now explicitly marks the methods `accounts.containers.destinations.get` and `accounts.containers.destinations.link` as deprecated. Developers currently relying on these endpoints to retrieve or link destinations within a GTM container should begin auditing their implementations and look for alternative workflows, as these methods are no longer recommended for long-term use.

**Tags:** `deprecation` `tag-manager` `containers`
