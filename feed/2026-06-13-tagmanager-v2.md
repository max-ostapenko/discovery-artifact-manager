---
date: 2026-06-13
api: tagmanager.v2
service: Google Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["tag-manager", "deprecation", "server-side-tagging"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-13  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has deprecated the get and link methods for container destinations, signaling a shift in how destination integrations are managed.

## Details

The API discovery document now explicitly flags accounts.containers.destinations.get and accounts.containers.destinations.link as deprecated. While these methods remain functional for now, their deprecation suggests that developers should look for alternative ways to manage container destinations, particularly in server-side tagging environments.

**Tags:** `tag-manager` `deprecation` `server-side-tagging`
