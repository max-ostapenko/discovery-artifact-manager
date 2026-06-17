---
date: 2026-06-17
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "authentication", "developer-connect"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-17  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports gitRepositoryLink in Git remote settings, allowing developers to use managed resource links for machine-based Git authentication.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, enabling a more structured way to handle machine credentials for Git operations within Dataform projects, likely integrating with Developer Connect for improved security and credential management.

**Tags:** `dataform` `git` `authentication` `developer-connect`
