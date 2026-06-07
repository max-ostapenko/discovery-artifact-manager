---
date: 2026-06-07
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "auth", "ci-cd"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-07  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports gitRepositoryLink within GitRemoteSettings, allowing developers to use specific resource links for machine-based Git authentication.

## Details

The GitRemoteSettings schema has been updated with a new optional field gitRepositoryLink. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*. This addition enables more robust machine-to-machine authentication by leveraging existing GitRepositoryLink resources instead of relying solely on manual credential configurations.

**Tags:** `dataform` `git` `auth` `ci-cd`
