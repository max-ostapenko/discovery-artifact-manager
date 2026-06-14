---
date: 2026-06-14
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Destination methods in GTM API"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Destination methods in GTM API

**Date:** 2026-06-14  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the get and link methods for the destinations resource within containers.

## Details

The API discovery document now explicitly flags accounts.containers.destinations.get and accounts.containers.destinations.link as deprecated. While these methods currently remain functional, developers should begin auditing their integrations to identify alternatives for destination management before these endpoints are eventually removed.

**Tags:** `deprecation` `tag-manager` `api-lifecycle`
