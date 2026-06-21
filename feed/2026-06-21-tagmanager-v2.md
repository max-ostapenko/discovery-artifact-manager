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

Google Tag Manager has deprecated the get and link methods for container destinations, signaling a shift in how tagging destinations are managed.

## Details

The API discovery document now explicitly marks the accounts.containers.destinations.get and accounts.containers.destinations.link methods as deprecated. Developers currently using these methods to retrieve or link destinations within GTM containers should begin looking for alternative workflows, as these methods are no longer recommended for long-term use.

**Tags:** `deprecation` `tag-manager`
