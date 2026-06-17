---
date: 2026-06-17
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "iam"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-17  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking to a GitRepositoryLink resource within GitRemoteSettings, enabling centralized machine credential management.

## Details

The GitRemoteSettings schema has been updated to include a new optional field, gitRepositoryLink. This field accepts a resource name following the pattern projects/*/locations/*/connections/*/gitRepositoryLinks/*. This addition allows developers to leverage managed connections for Git operations instead of manually handling secrets or personal access tokens within Dataform settings.

**Tags:** `dataform` `git` `security` `iam`
