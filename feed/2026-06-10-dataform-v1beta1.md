---
date: 2026-06-10
api: dataform.v1beta1
service: Dataform
title: "Dataform integrates GitRepositoryLink for machine auth"
impact: medium
breaking: false
tags: ["dataform", "git", "iam", "devops"]
interesting_score: 5
---

# Dataform integrates GitRepositoryLink for machine auth

**Date:** 2026-06-10  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports `gitRepositoryLink` in Git remote settings, enabling machine credential management via standard Google Cloud connection resources.

## Details

The `GitRemoteSettings` schema has been updated with a new optional `gitRepositoryLink` field. This field accepts a resource name in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`. This change allows developers to leverage Google Cloud's Developer Connect/Connections framework for Git authentication, providing a more standardized and secure way to handle machine credentials compared to manual secret management.

**Tags:** `dataform` `git` `iam` `devops`
