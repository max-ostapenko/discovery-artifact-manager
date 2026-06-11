---
date: 2026-06-11
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: low
breaking: false
tags: ["dataform", "git", "auth"]
interesting_score: 4
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-11  
**API:** `dataform.v1beta1`  
**Impact:** Low  

## Summary

Dataform's GitRemoteSettings now supports linking to GitRepositoryLink resources for machine credentials.

## Details

The `GitRemoteSettings` schema has been expanded with a new optional `gitRepositoryLink` field. This allows developers to point to a specific GitRepositoryLink resource (formatted as `projects/*/locations/*/connections/*/gitRepositoryLinks/*`) to handle machine-based authentication for Git operations, likely integrating with the broader Google Cloud Developer Connect ecosystem.

**Tags:** `dataform` `git` `auth`
