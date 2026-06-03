---
date: 2026-06-03
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "authentication", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-03  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform's GitRemoteSettings now supports a gitRepositoryLink field, enabling native resource-based authentication for Git operations.

## Details

The GitRemoteSettings schema has been updated to include an optional gitRepositoryLink field. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, allowing developers to leverage machine credentials via Google Cloud's connectivity services rather than relying solely on manual secret management for Git remotes.

**Tags:** `dataform` `git` `authentication` `devops`
