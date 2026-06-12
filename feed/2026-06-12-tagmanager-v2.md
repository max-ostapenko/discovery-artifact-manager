---
date: 2026-06-12
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Container Destination Methods"
impact: medium
breaking: false
tags: ["tagmanager", "deprecation"]
interesting_score: 5
---

# Deprecation of Container Destination Methods

**Date:** 2026-06-12  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the get and link methods for container destinations, signaling a shift in how tag destinations are managed.

## Details

The discovery document now flags `accounts.containers.destinations.get` and `accounts.containers.destinations.link` as deprecated. While these methods remain functional for now, their deprecation indicates that developers should begin looking for alternative ways to manage tag destinations within GTM containers, as these endpoints may be removed in a future revision.

**Tags:** `tagmanager` `deprecation`
