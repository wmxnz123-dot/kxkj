﻿# API 清单（对齐原型与联调）V1.0

本清单用于下一步原型到研发的接口对齐。V1 建议按“查询、提交、审核、配置、审计”分组；字段以“最小闭环”为主，后续可在接口评审时细化。

## 0. 通用约定
- 认证：用户端使用登录态 token；后台使用管理员登录态 token
- 统一响应结构（建议）：
  - code：业务码
  - message：提示信息
  - data：响应数据
- 分页（建议）：
  - pageNo、pageSize、total、list

## 1. 用户端（App）

### 1.1 首页/概览
- GET /app/overview
  - 入参：无
  - 出参：实名状态、资产统计（totalItems、toClaimCount、toFixCount）、最近动态列表

- GET /app/activities
  - 入参：pageNo、pageSize
  - 出参：动态列表（type、title、content、createdAt、jumpType、jumpId）

### 1.2 目录与认领
- GET /app/catalogs
  - 入参：keyword（可选）
  - 出参：目录树（catalogId、parentId、name、status统计）

- GET /app/catalog/{catalogId}/items
  - 入参：claimStatus（可选）、pageNo、pageSize
  - 出参：数据项列表（dataItemId、title、summary、updatedAt、claimStatus、correctStatus）

- GET /app/item/{dataItemId}
  - 出参：字段明细（fields）、来源信息（sourceSystem、updatedAt）、状态

- POST /app/claim
  - 入参：dataItemIds[] 或 catalogId（V1 建议先支持 dataItemIds）
  - 出参：成功/失败条目统计、失败原因列表（可选）

### 1.3 纠错
- POST /app/correction/ticket
  - 入参：dataItemId、fieldKey（可选）、originValue、correctedValue、reason、attachments[]
  - 出参：ticketId、status、createdAt

- GET /app/correction/tickets
  - 入参：status（可选）、pageNo、pageSize
  - 出参：工单列表（ticketId、objectName、status、createdAt、opinion摘要）

- GET /app/correction/ticket/{ticketId}
  - 出参：工单详情（原值/修正值/材料/状态/处理意见/轨迹）

- POST /app/correction/ticket/{ticketId}/supplement
  - 入参：attachments[]、remark（可选）
  - 出参：status、updatedAt

### 1.4 自有数据上传
- GET /app/upload/catalogs
  - 出参：自有目录树

- GET /app/upload/templates
  - 入参：catalogId（可选）
  - 出参：模板列表（templateId、name、fieldSchema、attachmentPolicy）

- POST /app/upload
  - 入参：catalogId、templateId、fields、attachments[]
  - 出参：uploadId、createdAt

- GET /app/uploads
  - 入参：catalogId（可选）、pageNo、pageSize
  - 出参：上传列表

- GET /app/upload/{uploadId}
  - 出参：详情（fields、attachments）

- DELETE /app/upload/{uploadId}
  - 出参：成功/失败

### 1.5 授权与服务
- GET /app/auth/requests
  - 入参：status（默认PENDING）、pageNo、pageSize
  - 出参：授权请求列表（requestId、requesterName、purpose、scope摘要、validity）

- GET /app/auth/request/{requestId}
  - 出参：请求详情 + 模板要点（riskTips、revokeTips、scope明细）

- POST /app/auth/decision
  - 入参：requestId、decision（GRANT/DENY）
  - 出参：authId、status

- GET /app/auth/records
  - 入参：status（可选）、pageNo、pageSize
  - 出参：授权记录列表

- GET /app/auth/record/{authId}
  - 出参：授权记录详情（scope快照、用途快照、有效期、撤销信息）

- POST /app/auth/revoke
  - 入参：authId
  - 出参：status=REVOKED、revokedAt

- GET /app/services
  - 入参：keyword（可选）、category（可选）
  - 出参：服务列表（serviceId、name、description、recommended、enabled）

- GET /app/service/{serviceId}
  - 出参：服务详情（requiredScope、entryUrl、授权提示）

## 2. 管理端（后台）

### 2.1 用户检索与档案
- GET /admin/users
  - 入参：name、idNo（可选）、communityId（可选）、pageNo、pageSize
  - 出参：用户列表（脱敏字段 + 统计）

- GET /admin/user/{userId}/profile
  - 出参：基础信息、目录统计、纠错摘要、授权摘要、自有数据摘要

### 2.2 目录与模板配置
- GET /admin/catalogs
- POST /admin/catalog
- PUT /admin/catalog/{catalogId}
- PATCH /admin/catalog/{catalogId}/enable

- GET /admin/catalog/{catalogId}/mappings
- POST /admin/catalog/{catalogId}/mapping
- PUT /admin/mapping/{mappingId}
- DELETE /admin/mapping/{mappingId}

- GET /admin/upload/catalogs
- POST /admin/upload/catalog
- GET /admin/upload/templates
- POST /admin/upload/template
- PUT /admin/upload/template/{templateId}
- PATCH /admin/upload/template/{templateId}/enable

### 2.3 授权模板与审计
- GET /admin/auth/templates
- POST /admin/auth/template
- PUT /admin/auth/template/{templateId}
- PATCH /admin/auth/template/{templateId}/enable

- GET /admin/auth/records
  - 入参：user、requester、scenario、status、timeRange、pageNo、pageSize
  - 出参：授权记录列表（可导出）

- GET /admin/auth/record/{authId}
  - 出参：详情 + 操作日志

- POST /admin/auth/records/export
  - 入参：筛选条件
  - 出参：导出任务ID或文件地址（按安全策略）

### 2.4 纠错审核
- GET /admin/corrections
  - 入参：status、keyword、timeRange、pageNo、pageSize
  - 出参：工单列表

- GET /admin/correction/{ticketId}
  - 出参：工单详情

- POST /admin/correction/{ticketId}/approve
  - 入参：action（修正/标注）、opinion
  - 出参：状态更新

- POST /admin/correction/{ticketId}/reject
  - 入参：opinion（必填）
  - 出参：状态更新

- POST /admin/correction/{ticketId}/need-more
  - 入参：opinion（必填）
  - 出参：状态更新

### 2.5 数据服务配置
- GET /admin/services
- POST /admin/service
- PUT /admin/service/{serviceId}
- PATCH /admin/service/{serviceId}/enable
- PATCH /admin/service/{serviceId}/sort

