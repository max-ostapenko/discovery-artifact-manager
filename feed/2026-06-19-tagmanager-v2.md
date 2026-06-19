---
date: 2026-06-19
api: tagmanager.v2
service: Tag Manager
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

Google Tag Manager has officially deprecated the 'get' and 'link' methods for container destinations, signaling a shift in how tagging destinations are managed.

## Details

The discovery document now explicitly marks 'accounts.containers.destinations.get' and 'accounts.containers.destinations.link' as deprecated. While these methods remain functional for now, developers building automation around GTM container configurations should begin looking for alternative management patterns, as these endpoints are likely slated for eventual removal.

**Tags:** `deprecation` `tag-manager`
