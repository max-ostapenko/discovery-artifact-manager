---
date: 2026-06-17
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-17  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking to GitRepositoryLink resources within GitRemoteSettings, streamlining machine credential management for Git operations.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*. This allows developers to use centralized repository links for authentication instead of managing credentials directly within Dataform settings, facilitating better integration with GCP's connection management services.

**Tags:** `dataform` `git` `security` `devops`
