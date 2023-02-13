tweet_body = {
                "match_mapping_type": "*",
                "mappings": {
                    "properties": {
                        "url": {"type": "text"},
                        "date": {"type": "date"},
                        "content": {"type": "text"},
                        "renderedContent": {"type": "text"},
                        "id": {"type": "keyword"},
                        "user": {
                            "properties": {
                                "username": {"type": "text"},
                                "id": {"type": "text"},
                                "displayname":  {"type": "text"},
                                "description":  {"type": "text"},
                                "rawDescription":  {"type": "text"},
                                "descriptionUrls":  {"type": "text"},
                                "verified": {"type": "text"},
                                "created": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss"},
                                "followersCount": {"type": "integer"},
                                "friendsCount": {"type": "integer"},
                                "statusesCount": {"type": "integer"},
                                "favouritesCount": {"type": "integer"},
                                "listedCount": {"type": "integer"},
                                "mediaCount": {"type": "integer"},
                                "location": {"type": "text"},
                                "protected": {"type": "text"},
                                "linkUrl": {"type": "text"},
                                "linkTcourl": {"type": "text"},
                                "profileImageUrl": {"type": "text"},
                                "profileBannerUrl": {"type": "text"},
                                "label": {"type": "text"}
                            }
                        },
                        "replyCount": {"type": "integer"},
                        "retweetCount": {"type": "integer"},
                        "likeCount": {"type": "integer"},
                        "quoteCount": {"type": "integer"},
                        "conversationId": {"type": "long"},
                        "lang": {"type": "text"},
                        "source": {"type": "text"},
                        "sourceUrl": {"type": "text"},
                        "sourceLabel": {"type": "text"},
                        "outlinks": {"type": "text"},
                        "tcooutlinks": {"type": "text"},
                        "media": {"type": "text"},
                        "retweetedTweet": {"type": "text"},
                        "quotedTweet": {"type": "text"},
                        "inReplyToTweetId": {"type": "text"},
                        "inReplyToUser": {"type": "text"},
                        "mentionedUsers": {"type": "text"},
                        "coordinates": {
                            "properties": {
                                "longitude": {"type": "geo_point"},
                                "latitude": {"type": "geo_point"}
                            }
                        },
                        "place": {
                            "properties": {
                                "fullName": {"type": "text"},
                                "name": {"type": "string"},
                                "type": {"type": "string"},
                                "country": {"type": "string"},
                                "countryCode": {"type": "string"}
                            }
                        },
                        "hashtags": {"type": "text"},
                        "cashtags": {"type": "text"}
                    },
                    "settings": {
                        "number_of_shards": 1,
                        "analysis": {
                            "normalizer": {
                                "hashtag_normalizer": {
                                    "type": "custom",
                                    "char_filter": [],
                                    "filter": ["lowercase", "asciifolding"]
                                }
                            }
                        }
                    }
                }
            }