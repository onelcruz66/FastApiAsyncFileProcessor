import os
import redis

redisSession = redis.Redis(host="localhost", port=6379, db=0)

def CacheStatus(fileId, status):
    redisSession.set(f"status: {fileId}", status, ex=3600)

def GetStatus(fileId):
    status = redisSession.get(f"status: {fileId}")
    return status.decode() if status else "unknown"