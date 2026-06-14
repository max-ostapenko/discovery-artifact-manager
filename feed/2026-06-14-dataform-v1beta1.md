---
date: 2026-06-14
api: dataform.v1beta1
service: Dataform
title: "Dataform adds Developer Connect support for Git"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "developer-connect"]
interesting_score: 5
---

# Dataform adds Developer Connect support for Git

**Date:** 2026-06-14  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports gitRepositoryLink in GitRemoteSettings, allowing developers to use machine credentials via Developer Connect.

## Details

The GitRemoteSettings schema has been updated with an optional gitRepositoryLink field. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, enabling more robust and centralized credential management for Git operations within Dataform by leveraging Google Cloud's Developer Connect service.

**Tags:** `dataform` `git` `security` `developer-connect`
