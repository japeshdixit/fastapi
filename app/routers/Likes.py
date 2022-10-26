from multiprocessing import synchronize
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import schemas, database, models, oAuth2
router = APIRouter(
    prefix="/like",
    tags=['Like']
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def like(like: schemas.Like, db: Session = Depends(database.get_db), current_user: int = Depends(oAuth2.get_current_user)):
    post=db.query(models.Post).filter(models.post.id==like.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,dtails=f"Post with id:{like.post_id} Does not Exists")
    like_query=db.query(models.Like).filter(models.Like.post_id ==
        like.post_id, models.Like.user_id == current_user.id)
    found_like=like_query.first()
    if (like.dir==1):
        if (found_like):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,default=f"user{current_user.id} has already liked the post {like.post_id}")
        new_like=models.Like(post_id=like.post_id,user_id=current_user.id)
        db.add(new_like)
        db.commit()
        return {"Message":"Liked this Post"}
    else:
        if not found_like:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Like Doesnot Exist")
        like_query.delete(synchronize_sessions=False)
        db.commit()
        return {"Message":"Successfully Deleted Like"}

