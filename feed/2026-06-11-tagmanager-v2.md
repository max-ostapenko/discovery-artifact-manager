---
date: 2026-06-11
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-11  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for container destinations, signaling a shift in how external destinations are managed.

## Details

The discovery document now flags 'accounts.containers.destinations.get' and 'accounts.containers.destinations.link' as deprecated. While these methods currently remain functional, developers should audit their integrations and prepare for these endpoints to be phased out in favor of newer configuration patterns.

**Tags:** `deprecation` `tag-manager` `api-lifecycle`
