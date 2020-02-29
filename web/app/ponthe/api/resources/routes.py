import re
import os
import datetime
import json

from flask_restplus import Resource
from flask import request, redirect, send_file
from itsdangerous import SignatureExpired, BadSignature

from . import api
from ... import db, app
from ...services import FileService
from ...dao import FileDAO, GalleryDAO

ASSET_FOLDER = app.config['ASSET_ROOT']


@api.route('/get-video/<gallery_slug>')
@api.doc(params={
    'gallery_slug': 'the video gallery which owns the video you want'
})
class GetVideo(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Request incorrect - JSON not valid')
    @api.response(403, 'Not authorized - account not valid')
    def get(self, gallery_slug: str):
        '''Get the video which is in some gallery with slug gallery_slug'''
        video = FileDAO.get_video_from_gallery_slug(gallery_slug)

        return send_file(
            open(FileService.get_absolute_file_path(video), "rb"),
            mimetype='video/' + video.extension
            )


@api.route('/get-video-cover-image/<gallery_slug>')
@api.doc(params={
    'gallery_slug': 'the video gallery which owns the video you want'
})
class GetVideoCoverImage(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Request incorrect - JSON not valid')
    @api.response(403, 'Not authorized - account not valid')
    def get(self, gallery_slug: str):
        '''Get the video cover image in some gallery with slug gallery_slug'''
        gallery = GalleryDAO().find_by_slug(gallery_slug)
        cover_image = FileDAO().get_cover_image_of_video_gallery(gallery)
        if cover_image is not None:
            return send_file(
                open(FileService.get_absolute_file_path(cover_image), "rb"),
                mimetype='image/' + cover_image.extension
                )
        else:
            return { "msg": "The video has no cover image" }, 200