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

Dataform now supports linking to managed Git repository resources for machine-based authentication via the new gitRepositoryLink field.

## Details

The `GitRemoteSettings` schema has been updated with an optional `gitRepositoryLink` field. This allows developers to reference a specific Git connection resource (format: `projects/*/locations/*/connections/*/gitRepositoryLinks/*`) instead of relying solely on manual credential configurations. This change points toward better integration with Google Cloud's centralized connection management services, simplifying how Dataform workspaces authenticate with external repositories.

**Tags:** `dataform` `git` `security` `iam`
