---
date: 2026-06-06
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "iam"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-06  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking to GitRepositoryLink resources for Git remote settings, enabling centralized machine credential management.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*. This allows developers to leverage the standard GCP Developer Connect/Cloud Build v2 connection ecosystem for Git authentication rather than managing standalone credentials within Dataform.

**Tags:** `dataform` `git` `security` `iam`
