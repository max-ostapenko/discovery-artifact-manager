---
date: 2026-06-13
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: low
breaking: false
tags: ["dataform", "git", "authentication", "devops"]
interesting_score: 4
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-13  
**API:** `dataform.v1beta1`  
**Impact:** Low  

## Summary

Dataform's Git settings now support a gitRepositoryLink field for managed repository connections.

## Details

The GitRemoteSettings schema has been updated to include an optional gitRepositoryLink field. This string field allows developers to reference a specific GitRepositoryLink resource (formatted as projects/*/locations/*/connections/*/gitRepositoryLinks/*), facilitating the use of machine credentials for Git operations instead of relying solely on manual token or SSH configurations.

**Tags:** `dataform` `git` `authentication` `devops`
