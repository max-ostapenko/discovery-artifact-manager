---
date: 2026-06-19
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "containers"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-19  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has deprecated the get and link methods for container destinations, signaling a shift in how external destinations are managed.

## Details

The API discovery document now explicitly marks the accounts.containers.destinations.get and accounts.containers.destinations.link methods as deprecated. While these methods currently remain functional, developers should audit their integrations and watch for alternative patterns for managing container-to-destination linkages.

**Tags:** `deprecation` `tag-manager` `containers`
