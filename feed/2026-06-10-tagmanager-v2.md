---
date: 2026-06-10
api: tagmanager.v2
service: Google Tag Manager
title: "Deprecation of Destination methods in Tag Manager"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "destinations"]
interesting_score: 6
---

# Deprecation of Destination methods in Tag Manager

**Date:** 2026-06-10  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the get and link methods for the destinations resource, signaling a shift in how container destinations are managed.

## Details

The discovery document now explicitly flags accounts.containers.destinations.get and accounts.containers.destinations.link as deprecated. While these methods currently remain functional, the deprecation notice indicates that developers should begin transitioning away from these specific endpoints for retrieving or linking destinations within GTM containers.

**Tags:** `deprecation` `tag-manager` `destinations`
