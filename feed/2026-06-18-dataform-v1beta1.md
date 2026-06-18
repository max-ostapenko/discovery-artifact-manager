---
date: 2026-06-18
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "credentials"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-18  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking GitRepositoryLink resources to GitRemoteSettings, enabling more streamlined machine credential management for Git integrations.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field accepts a resource name in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`, allowing developers to leverage managed connections for Git operations rather than manually managing secrets or personal access tokens within Dataform.

**Tags:** `dataform` `git` `security` `credentials`
