---
date: 2026-06-10
api: tagmanager.v2
service: Google Tag Manager
title: "Deprecation of Destination methods in Tag Manager"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager"]
interesting_score: 5
---

# Deprecation of Destination methods in Tag Manager

**Date:** 2026-06-10  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for the Destinations resource within containers.

## Details

The API discovery document now flags accounts.containers.destinations.get and accounts.containers.destinations.link as deprecated. While these methods are still present in the v2 surface, developers should prepare for their eventual removal and look for alternative ways to manage destination configurations within GTM containers.

**Tags:** `deprecation` `tag-manager`
