---
date: 2026-06-13
api: tagmanager.v2
service: Tag Manager
title: "Container Destination methods marked as deprecated"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "api-lifecycle"]
interesting_score: 5
---

# Container Destination methods marked as deprecated

**Date:** 2026-06-13  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for container destinations, signaling a shift in how external destinations are managed.

## Details

The methods `accounts.containers.destinations.get` and `accounts.containers.destinations.link` have been updated with a `deprecated: true` flag in the discovery document. While these methods remain functional for now, their deprecation suggests that developers should look for alternative ways to manage container destinations or prepare for these endpoints to be removed in a future revision.

**Tags:** `deprecation` `tag-manager` `api-lifecycle`
