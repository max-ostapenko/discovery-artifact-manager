---
date: 2026-06-07
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "iam", "credentials"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-07  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking Git repositories via the GitRepositoryLink resource, enabling more streamlined machine credential management.

## Details

A new optional field `gitRepositoryLink` has been added to the `GitRemoteSettings` schema. This field allows developers to specify a resource name in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`, facilitating the use of centralized Git connections for authentication instead of managing credentials directly within Dataform.

**Tags:** `dataform` `git` `iam` `credentials`
