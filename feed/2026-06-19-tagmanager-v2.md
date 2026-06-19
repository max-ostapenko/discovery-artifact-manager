---
date: 2026-06-19
api: tagmanager.v2
service: Google Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-19  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has deprecated the get and link methods for container destinations, signaling a shift in how tag destinations are managed.

## Details

The API discovery document now explicitly marks the `accounts.containers.destinations.get` and `accounts.containers.destinations.link` methods as deprecated. Developers currently relying on these endpoints for managing or retrieving destination links within GTM containers should begin looking for alternative workflows, as these methods are likely slated for eventual removal.

**Tags:** `deprecation` `tag-manager`
