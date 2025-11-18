# Current Caching Implementation

## Overview

Our web application currently uses a simple file-based caching system implemented in Node.js. This document describes the current approach and its limitations.

## Implementation Details

### Cache Storage

Location: `src/cache/file-cache.js`

We store cached data as JSON files in the filesystem:

```javascript
// File: src/cache/file-cache.js (lines 12-45)
const fs = require('fs');
const path = require('path');

const CACHE_DIR = path.join(__dirname, '../../cache-data');

class FileCache {
  constructor() {
    if (!fs.existsSync(CACHE_DIR)) {
      fs.mkdirSync(CACHE_DIR, { recursive: true });
    }
  }

  get(key) {
    const filePath = path.join(CACHE_DIR, `${key}.json`);

    if (!fs.existsSync(filePath)) {
      return null;
    }

    try {
      const data = fs.readFileSync(filePath, 'utf8');
      const cached = JSON.parse(data);

      // Check expiration
      if (cached.expiresAt && cached.expiresAt < Date.now()) {
        this.delete(key);
        return null;
      }

      return cached.value;
    } catch (error) {
      console.error(`Cache read error for key ${key}:`, error);
      return null;
    }
  }

  set(key, value, ttlSeconds = 3600) {
    const filePath = path.join(CACHE_DIR, `${key}.json`);
    const data = {
      value,
      expiresAt: Date.now() + (ttlSeconds * 1000)
    };

    try {
      fs.writeFileSync(filePath, JSON.stringify(data));
      return true;
    } catch (error) {
      console.error(`Cache write error for key ${key}:`, error);
      return false;
    }
  }

  delete(key) {
    const filePath = path.join(CACHE_DIR, `${key}.json`);
    if (fs.existsSync(filePath)) {
      fs.unlinkSync(filePath);
    }
  }

  clear() {
    if (fs.existsSync(CACHE_DIR)) {
      const files = fs.readdirSync(CACHE_DIR);
      files.forEach(file => {
        fs.unlinkSync(path.join(CACHE_DIR, file));
      });
    }
  }
}

module.exports = new FileCache();
```

### Current Usage

We use caching for:

1. **API responses** (60-second TTL)
2. **Database query results** (5-minute TTL)
3. **Rendered HTML fragments** (30-minute TTL)
4. **Static asset manifests** (24-hour TTL)

Example usage in API handler:

```javascript
// File: src/api/users.js (lines 8-25)
const cache = require('../cache/file-cache');

async function getUser(userId) {
  const cacheKey = `user:${userId}`;

  // Try cache first
  const cached = cache.get(cacheKey);
  if (cached) {
    return cached;
  }

  // Cache miss - fetch from database
  const user = await db.users.findById(userId);

  // Cache for 5 minutes
  cache.set(cacheKey, user, 300);

  return user;
}
```

## Performance Characteristics

### Current Metrics

- **Cache hit rate**: ~65%
- **Average cache read time**: 25-40ms
- **Average cache write time**: 15-30ms
- **Cache miss penalty**: 150-200ms (database query)

### Performance Issues

1. **Slow read times**: File I/O is slower than in-memory cache
   - Reading JSON file: 25-40ms
   - Parsing JSON: 5-10ms
   - Total: 30-50ms per cache read

2. **Concurrent access issues**: No locking mechanism
   - Multiple writes to same key can cause corruption
   - Race conditions between read/write operations

3. **Disk space growth**: No automatic cleanup
   - Expired entries not automatically deleted
   - Cache directory grows to 2GB+ over time
   - Manual cleanup required weekly

4. **No distributed caching**: Single server only
   - Each server has its own cache
   - No cache sharing across servers
   - Cache warming required on each deploy

## Scalability Limitations

### Current Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Server 1   │     │  Server 2   │     │  Server 3   │
│             │     │             │     │             │
│ File Cache  │     │ File Cache  │     │ File Cache  │
│ (isolated)  │     │ (isolated)  │     │ (isolated)  │
└─────────────┘     └─────────────┘     └─────────────┘
```

### Problems

1. **No cache sharing**: Each server maintains independent cache
2. **Memory waste**: Same data cached 3 times (once per server)
3. **Inconsistency**: Cache invalidation only affects one server
4. **Poor hit rate**: Cold start on each server after deploy

## Operational Issues

### Deployment Impact

- **Cache loss on deploy**: All cached data lost when server restarts
- **Cold start period**: First 10-15 minutes after deploy have slow responses
- **Manual cache warming**: Need to pre-warm cache with common queries

### Maintenance Burden

- **Manual cleanup**: Weekly cron job to delete expired cache files
- **Disk space monitoring**: Alert when cache directory > 5GB
- **No visibility**: Can't see cache hit/miss rates in real-time

### Error Scenarios

- **Disk full**: Cache writes fail silently, no fallback
- **File corruption**: Invalid JSON causes cache read errors
- **Permission issues**: Cache fails if directory permissions wrong

## Cost Analysis

### Infrastructure Cost

- **Disk space**: 10GB allocated per server for cache
- **I/O operations**: ~1000 reads/sec, ~200 writes/sec per server
- **Monthly cost**: Negligible (using existing server disk)

### Development Cost

- **Initial implementation**: 2 developer-days
- **Ongoing maintenance**: 2-3 hours/month for cleanup and monitoring
- **Debugging time**: ~1 hour/week troubleshooting cache-related issues

## Summary

The current file-based caching system works for our initial needs but has significant limitations:

✅ **Pros**:
- Simple implementation
- No external dependencies
- Low infrastructure cost
- Easy to debug (just read JSON files)

❌ **Cons**:
- Slow performance (30-50ms per read)
- No distributed caching
- High maintenance burden
- Scalability limitations
- No real-time monitoring

## Recommendation

We need a more scalable caching solution to support:
1. Sub-10ms cache read times
2. Distributed caching across servers
3. Automatic expiration and cleanup
4. Real-time monitoring and metrics
5. Support for 10,000+ requests/second
