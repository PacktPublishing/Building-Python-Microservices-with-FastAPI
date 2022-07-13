async def check_post_owner(feedbacks, fid, touristId):
    return feedbacks[fid].tourist_id == touristId