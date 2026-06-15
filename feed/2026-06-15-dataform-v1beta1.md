---
date: 2026-06-15
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "authentication", "iam"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-15  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports gitRepositoryLink within Git remote settings, allowing developers to use managed repository links for machine authentication.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*. This change simplifies credential management by allowing Dataform to leverage centralized Git repository connections (likely via Developer Connect) instead of manually managing secrets for machine-to-machine authentication.

**Tags:** `dataform` `git` `authentication` `iam`
