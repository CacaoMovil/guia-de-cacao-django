# -*- coding: utf-8 -*-
import os
import re
import logging
import mimetypes
import hashlib
import json
import time
import calendar

from django.conf import settings
from django.test.client import Client

from django_perseus.exceptions import RendererException
from django_perseus.renderers.base import BaseRenderer
from django_perseus.renderers.default import DefaultRenderer
from django.core.urlresolvers import reverse

from .models import Guide, Content
from .serializers import GuidesSerializer

logger = logging.getLogger('perseus')


class GuideRenderer(BaseRenderer):

    """
    This serializer extend from Django perseus - BaseRenderer
    this serializer convert the name of a url to hashlib and
    append the web file extention.
    """
    regex = re.compile("^/guia/(?P<pk>\d+)/$")

    def render_path(self, path=None, view=None):
        if path:
            # create deploy dir if not exists
            deploy_dir = settings.PERSEUS_SOURCE_DIR
            outpath = os.path.join(deploy_dir, '')
            android_filename = ".nomedia"
            manifest_filename = "manifest.json"
            if not os.path.exists(deploy_dir):
                os.makedirs(deploy_dir)

            # create the no media file for the android app
            nomedia_dir = os.path.join(deploy_dir, android_filename)
            nomedia_file = open(nomedia_dir, "w")
            nomedia_file.close()

            # create the Manifest file for the android app
            manifest_dir = os.path.join(deploy_dir, manifest_filename)
            manifest_file = open(manifest_dir, "w")
            json.dump(self.create_manifest(), manifest_file, indent=4)
            manifest_file.close()

            # create the renders page
            if self.regex.findall(path):
                response, mime = self.render_page(path)
                outpath = os.path.join(outpath, 'index{0}'.format(mime))
                self.save_page(response, outpath)
                return
            else:
                response, mime = self.render_page(path)
                name = '%s.html' % hashlib.sha1(path).hexdigest()
                outpath = os.path.join(deploy_dir, name)
                self.save_page(response, outpath)
                return

    def render_page(self, path):
        response = self.client.get(path)
        if response.status_code is not 200:
            raise RendererException(
                'Path: {0} returns status code: {1}.'.format(path, response.status_code))
        return response, self.get_mime(response)

    def get_mime(self, response):
        mime = response['Content-Type']
        encoding = mime.split(';', 1)[0]
        return mimetypes.guess_extension(encoding)

    def save_page(self, response, outpath):
        logger.debug(outpath)
        with open(outpath, 'wb') as f:
            f.write(response.content)

    def generate(self):
        self.client = Client()
        for path in self.paths():
            self.render_path(path=path)


def date_handler(obj):
    """
    Simple python handler that conver
    a datetime.date to human date
    """
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


class HomeRenderer(GuideRenderer):

    """
    This class make the render from dinamic pages,
    the filter is from the base command
    """

    def __init__(self, guide_number=None):
        self.guide_number = guide_number

    def create_manifest(self):
        """
        Simple method that return our manifest
        dict used in the manifest.json
        """
        guides = Guide.objects.all()
        serializer = GuidesSerializer(guides, many=True)
        content = json.dumps(serializer.data, default=date_handler, indent=4)
        manifest_dict = {
            "manifest_version": 1,
            "guide_id": self.guide_number,
            "guide_version": self.guide_number,
            'generation_date': calendar.timegm(time.gmtime()),
            'contents': json.loads(content)
        }
        return manifest_dict

    def paths(self):
        paths = set([])
        if self.guide_number:
            guides = Guide.objects.filter(number=self.guide_number)
            contents = Content.objects.filter(section__guide=self.guide_number)
        else:
            guides = Guide.objects.all()
            contents = Content.objects.all()

        for guide in guides:
            paths.add(guide.get_absolute_url())
        for content in contents:
            paths.add(content.get_absolute_url())

        return paths

class AboutUsRenderer(DefaultRenderer):

    def paths(self):
        return [reverse('about')]

renderers = [HomeRenderer, ]
