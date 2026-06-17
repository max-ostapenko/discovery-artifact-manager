---
date: 2026-06-17
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-17  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for container destinations, signaling a shift in how destination integrations are managed.

## Details

The discovery document now flags 'accounts.containers.destinations.get' and 'accounts.containers.destinations.link' with 'deprecated: true'. While these methods remain functional for the time being, developers should audit their implementations and prepare for these endpoints to be phased out in favor of newer integration patterns.

**Tags:** `deprecation` `tag-manager` `api-lifecycle`
