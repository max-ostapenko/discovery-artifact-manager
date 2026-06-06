---
date: 2026-06-06
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-06  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking GitRepositoryLink resources within GitRemoteSettings, enabling better management of machine credentials for Git operations.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field allows developers to specify a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, which is used to handle machine credentials for Git connectivity. This likely integrates with GCP's Developer Connect for more secure, managed repository access.

**Tags:** `dataform` `git` `security` `devops`
