---
date: 2026-06-14
api: tagmanager.v2
service: Tag Manager
title: "Tag Manager deprecates Destination get and link methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "analytics"]
interesting_score: 5
---

# Tag Manager deprecates Destination get and link methods

**Date:** 2026-06-14  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

The Tag Manager API has officially deprecated the `get` and `link` methods within the `destinations` resource, signaling a future removal.

## Details

The discovery document now flags `accounts.containers.destinations.get` and `accounts.containers.destinations.link` as deprecated. These methods are typically used for managing the connection between GTM containers and external destinations like Google Analytics 4. Developers currently relying on these endpoints should begin auditing their implementations to identify alternative workflows before these methods are fully decommissioned.

**Tags:** `deprecation` `tag-manager` `analytics`
