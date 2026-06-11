---
date: 2026-06-11
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "iam"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-11  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking directly to GitRepositoryLink resources for authentication, streamlining machine credential management.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*. This addition allows developers to leverage managed connection resources for Git operations, potentially simplifying how machine-user credentials are handled and rotated within Dataform projects.

**Tags:** `dataform` `git` `security` `iam`
