---
date: 2026-06-15
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "devops", "bigquery"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-15  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports referencing a GitRepositoryLink resource within GitRemoteSettings, enabling more structured machine credential management.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*. This allows developers to link Dataform workspaces to specific Git repository connection resources, streamlining authentication and repository management for automated workflows and machine-to-machine integrations.

**Tags:** `dataform` `git` `devops` `bigquery`
