---
date: 2026-06-05
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "auth", "developer-connect"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-05  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking GitRepositoryLink resources directly in GitRemoteSettings, streamlining machine-to-machine authentication for Git operations.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*. This allows developers to leverage centralized connection management for Git credentials rather than relying solely on manual secret configurations, facilitating better integration with Developer Connect.

**Tags:** `dataform` `git` `auth` `developer-connect`
