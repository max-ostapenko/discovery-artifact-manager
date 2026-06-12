---
date: 2026-06-12
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "authentication", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-12  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking to a specific GitRepositoryLink resource within GitRemoteSettings for machine-based authentication.

## Details

The `GitRemoteSettings` schema has been updated with a new optional field: `gitRepositoryLink`. This field accepts a resource name in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`. This addition allows developers to leverage managed repository connections for Git operations, likely integrating with GCP's Developer Connect service to handle machine credentials more securely and natively.

**Tags:** `dataform` `git` `authentication` `devops`
