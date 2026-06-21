---
date: 2026-06-21
api: tagmanager.v2
service: Google Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-21  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for container destinations, signaling a shift in how external integrations are managed.

## Details

The discovery document now explicitly marks the `accounts.containers.destinations.get` and `accounts.containers.destinations.link` methods as deprecated. While these methods currently remain functional, their deprecation suggests that developers should begin looking for alternative ways to manage destination configurations within GTM containers before these endpoints are eventually retired.

**Tags:** `deprecation` `tag-manager`
