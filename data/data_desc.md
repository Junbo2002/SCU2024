# 数据集描述

## 数据库表设计

### 实体

#### album 专辑表
> 发行专辑的信息


| 表名    | 字段名   | 描述 |
|-------|-------|----|
| album | id    |    |
| album | MDID  |    |
| album | title |    |

#### person 艺人表
> 音乐人等

| 表名     | 字段名  | 描述 |
|--------|------|----|
| person | id   |    |
| person | MDID |    |
| person | name |    |

#### track 歌曲表
> 歌曲信息

| 表名    | 字段名       | 描述 |
|-------|-----------|----|
| track | id        |    |
| track | person_id |    |
| track | album_id  |    |
| track | MDID      |    |
| track | name      |    |
| track | playcount |    |
| track | duration  |    |

#### tag 标签表
> 歌曲类型标签

| 表名  | 字段名   | 描述 |
|-----|-------|----|
| tag | id    |    |
| tag | value |    |

#### user 用户表
> 用户信息

| 表名   | 字段名             | 描述 |
|------|-----------------|----|
| user | id              |    |
| user | lastfm_username |    |
| user | gender          |    |
| user | age             |    |
| user | country         |    |
| user | playcount       |    |
| user | playlists       |    |
| user | subscribertype  |    |

#### preference 用户偏好表
> 用户喜欢的歌曲

| 表名         | 字段名      | 描述 |
|------------|----------|----|
| preference | id       |    |
| preference | user_id  |    |
| preference | track_id |    |

#### playlist 歌单表
> 用户创建的歌单

| 表名       | 字段名        | 描述 |
|----------|------------|----|
| playlist | id         |    |
| playlist | creator_id |    |
| playlist | title      |    |
| playlist | numtrack   |    |
| playlist | duration   |    |

### 关系

#### event

#### session

#### track_tag 歌曲标签关系表

#### playlist_track

#### session_track