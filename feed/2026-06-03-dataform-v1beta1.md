---
date: 2026-06-03
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "auth"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-03  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking Git repositories via a specific GitRepositoryLink resource, enabling better management of machine credentials.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field allows developers to specify a resource name (following the pattern projects/*/locations/*/connections/*/gitRepositoryLinks/*) to handle machine credentials for Git operations, providing a more structured way to manage repository connections compared to traditional auth methods.

**Tags:** `dataform` `git` `auth`
