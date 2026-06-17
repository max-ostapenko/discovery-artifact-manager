---
date: 2026-06-17
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "auth", "security"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-17  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports using GitRepositoryLink resources for Git remote settings, enabling more streamlined machine credential management.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, allowing developers to link specific connection resources for authentication instead of relying solely on manual secret management.

**Tags:** `dataform` `git` `auth` `security`
