---
date: 2026-06-08
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "credentials"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-08  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking to GitRepositoryLink resources for machine credentials in Git remote settings, improving credential management.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field allows developers to specify a resource name (following the format projects/*/locations/*/connections/*/gitRepositoryLinks/*) to handle machine credentials for Git operations, likely facilitating better integration with Google Cloud's connectivity and secret management services.

**Tags:** `dataform` `git` `security` `credentials`
