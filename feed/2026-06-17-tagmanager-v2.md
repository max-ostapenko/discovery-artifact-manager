---
date: 2026-06-17
api: tagmanager.v2
service: Google Tag Manager
title: "Deprecation of Container Destination Methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager"]
interesting_score: 5
---

# Deprecation of Container Destination Methods

**Date:** 2026-06-17  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for container destinations, signaling a shift in how tag destinations are managed.

## Details

The API discovery document now flags `accounts.containers.destinations.get` and `accounts.containers.destinations.link` as deprecated. This affects developers programmatically managing Google Tag destinations within GTM containers. While the methods are still present, their use is discouraged in favor of newer tagging integration patterns.

**Tags:** `deprecation` `tag-manager`
