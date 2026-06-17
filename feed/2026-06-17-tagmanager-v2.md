---
date: 2026-06-17
api: tagmanager.v2
service: Google Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager"]
interesting_score: 6
---

# Deprecation of Container Destination methods

**Date:** 2026-06-17  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has deprecated the 'get' and 'link' methods for container destinations, signaling a shift in how tag destinations are managed.

## Details

The API discovery document now explicitly marks the methods `accounts.containers.destinations.get` and `accounts.containers.destinations.link` as deprecated. While these methods currently remain functional, developers should begin auditing their automation scripts and integrations to move away from these specific destination management endpoints.

**Tags:** `deprecation` `tag-manager`
