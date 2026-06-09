---
date: 2026-06-09
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "iam"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-09  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking to GitRepositoryLink resources within GitRemoteSettings, enabling better management of machine credentials for remote repositories.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field allows developers to specify a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, facilitating the use of centralized connection management for Git authentication rather than relying on manual credential configurations.

**Tags:** `dataform` `git` `security` `iam`
