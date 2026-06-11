---
date: 2026-06-11
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "authentication"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-11  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform's GitRemoteSettings now supports gitRepositoryLink, enabling centralized machine credential management for Git operations.

## Details

The GitRemoteSettings schema has been updated with an optional gitRepositoryLink field. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*. This change allows Dataform to leverage the Service Connection/Developer Connect framework for secure Git repository access, facilitating better machine-to-machine authentication without manual secret handling.

**Tags:** `dataform` `git` `security` `authentication`
