---
date: 2026-06-11
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "authentication"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-11  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking to GitRepositoryLink resources for machine-based authentication within GitRemoteSettings.

## Details

The `GitRemoteSettings` schema has been updated with an optional `gitRepositoryLink` field. This field accepts a resource name in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`, enabling developers to leverage Google Cloud's connection-based repository linking for machine credentials rather than managing secrets manually.

**Tags:** `dataform` `git` `authentication`
