---
date: 2026-06-16
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "auth", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-16  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking Git repositories via the GitRepositoryLink resource, streamlining machine credential management.

## Details

The GitRemoteSettings schema now includes an optional gitRepositoryLink field. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, allowing developers to leverage centralized connection management for Git authentication instead of relying on legacy credential methods.

**Tags:** `dataform` `git` `auth` `devops`
