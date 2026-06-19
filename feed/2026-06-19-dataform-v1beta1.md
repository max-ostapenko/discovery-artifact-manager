---
date: 2026-06-19
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "authentication", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-19  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform's Git configuration now supports direct linking to GitRepositoryLink resources for authentication.

## Details

The `GitRemoteSettings` schema has been updated with a new optional field: `gitRepositoryLink`. This field allows developers to specify a resource name (following the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`) to handle machine credentials, likely integrating with Google Cloud's Developer Connect or similar managed connection services.

**Tags:** `dataform` `git` `authentication` `devops`
