---
date: 2026-06-08
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "authentication", "developer-connect"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-08  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking GitRepositoryLink resources directly within GitRemoteSettings, streamlining machine-to-machine authentication for Git repositories.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*. This allows developers to leverage managed connections for Git authentication, likely integrating with Developer Connect, instead of relying solely on manual credential configurations.

**Tags:** `dataform` `git` `authentication` `developer-connect`
