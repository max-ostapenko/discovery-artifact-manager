---
date: 2026-06-05
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "authentication", "developer-connect"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-05  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking to a GitRepositoryLink resource within GitRemoteSettings, enabling more structured machine credential management for Git operations.

## Details

The GitRemoteSettings schema has been updated to include an optional gitRepositoryLink field. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, allowing developers to point to specific repository connections for authentication rather than relying solely on manual credential configurations. This likely integrates with Google Cloud's Developer Connect for more secure, managed Git access.

**Tags:** `dataform` `git` `authentication` `developer-connect`
