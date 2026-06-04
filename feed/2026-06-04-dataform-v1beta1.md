---
date: 2026-06-04
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "authentication"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-04  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking Git repositories via the GitRepositoryLink resource, enabling more streamlined machine credential management.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, allowing developers to leverage centralized Git repository connections for automated workflows and machine-based authentication instead of managing individual secrets manually.

**Tags:** `dataform` `git` `authentication`
