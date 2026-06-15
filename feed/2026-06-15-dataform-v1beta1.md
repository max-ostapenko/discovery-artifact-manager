---
date: 2026-06-15
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "iam"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-15  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking to GitRepositoryLink resources within GitRemoteSettings, enabling more streamlined machine credential management.

## Details

The `GitRemoteSettings` schema has been updated with a new optional field: `gitRepositoryLink`. This field allows developers to specify a resource name (following the `projects/*/locations/*/connections/*/gitRepositoryLinks/*` pattern) to handle machine credentials. This addition likely facilitates better integration with Google Cloud's connectivity services for secure Git authentication without manual secret handling.

**Tags:** `dataform` `git` `security` `iam`
