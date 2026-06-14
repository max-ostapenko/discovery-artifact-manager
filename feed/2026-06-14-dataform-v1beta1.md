---
date: 2026-06-14
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["git", "authentication", "security", "dataform"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-14  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports GitRepositoryLink resources for Git remote authentication, enabling integration with managed connection services.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, allowing developers to leverage machine credentials managed via Google Cloud's connection services for Git operations rather than manual credential management.

**Tags:** `git` `authentication` `security` `dataform`
